from librs.datasets import make_dataset, make_data_loader
import os

train_dataset = make_dataset(
    'jump', True, ['training'], json_file='./data/jump/annotations/Jump_label.json',
    feat_folder='./data/jump/i3d_features',
    file_prefix='',
    file_ext='.npz',
    num_classes=1,
    input_dim=2048,
    feat_stride=32,
    num_frames=16,
    default_fps=30,
    trunc_thresh=0.5,
    crop_ratio=[0.9, 1.0],
    max_seq_len=768,
    downsample_rate=1,
    force_upsampling=True)
# update cfg based on dataset attributes (fix to epic-kitchens)
print(len(train_dataset))
train_db_vars = train_dataset.get_attributes()
print(train_db_vars)
