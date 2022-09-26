# python imports
import argparse
import os
import glob
import time
from pprint import pprint

import numpy as np
# torch imports
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torch.utils.data

# our code
from librs.core import load_config
from librs.datasets import make_dataset, make_data_loader
from librs.modeling import make_meta_arch
from librs.utils import valid_one_epoch, ANETdetection, fix_random_seed

################################################################################

def main(file='./data/sit/i3d_features/20220628001-rgb.npz', config='configs/sit.yaml', ckpt='models/best_ckpt/jump_i3d_reproduce/epoch_059.pth.tar'):
    """0. load config"""
    # sanity check
    if os.path.isfile(config):
        cfg = load_config(config)
    else:
        raise ValueError("Config file does not exist.")
    assert len(cfg['val_split']) > 0, "Test set must be specified!"
    if ".pth.tar" in ckpt:
        assert os.path.isfile(ckpt), "CKPT file does not exist!"
        ckpt_file = ckpt
    else:
        assert os.path.isdir(ckpt), "CKPT file folder does not exist!"
        ckpt_file_list = sorted(glob.glob(os.path.join(ckpt, '*.pth.tar')))
        ckpt_file = ckpt_file_list[-1]


    """1. fix all randomness"""
    # fix the random seeds (this will fix everything)
    _ = fix_random_seed(0, include_cuda=True)

    """2. create data"""
    video= np.load(file)
    print(video.shape)
    video = torch.from_numpy(video).float()
    # video = video.unsqueeze(0)




    """3. create model"""
    model = make_meta_arch(cfg['model_name'], **cfg['model'])
    # not ideal for multi GPU training, ok for now
    model = nn.DataParallel(model, device_ids=cfg['devices'])

    """4. load ckpt"""
    print("=> loading checkpoint '{}'".format(ckpt_file))
    # load ckpt, reset epoch / best rmse
    checkpoint = torch.load(
        ckpt_file,
        map_location=lambda storage, loc: storage.cuda(cfg['devices'][0])
    )
    # load ema model instead
    print("Loading from EMA model ...")
    model.load_state_dict(checkpoint['state_dict_ema'])
    del checkpoint

    video = video.to(cfg['devices'][0])

    video_list={'feats': video}
    video_list = [video_list]
    """5. inference"""
    print("=> inference ...")
    start = time.time()
    model.eval()

    results = {
        'video-id': [],
        't-start' : [],
        't-end': [],
        'label': [],
        'score': []
    }
    with torch.no_grad():
        output = model(video_list)
        print(output)
        num_vids = len(output)
        for vid_idx in range(num_vids):
            if output[vid_idx]['segments'].shape[0] > 0:
                results['video-id'].extend(
                    [output[vid_idx]['video_id']] *
                    output[vid_idx]['segments'].shape[0]
                )
                results['t-start'].append(output[vid_idx]['segments'][:, 0])
                results['t-end'].append(output[vid_idx]['segments'][:, 1])
                results['label'].append(output[vid_idx]['labels'])
                results['score'].append(output[vid_idx]['scores'])

    print("=> inference done in {:.2f} seconds".format(time.time() - start))
    print(results)
    ################################################################################
if __name__ == '__main__':
    """Entry Point"""

    main(file='data/20220628001_r21d.npy',
         config='configs/sit.yaml',
         ckpt='models/epoch_059.pth.tar')