import numpy as np
import json
import pickle


# file1='./data/v___c8enCfzqw.npy'
# file2='./data/video_test_0000004.npy'
# file2_1='./data/video_test_0000006.npy'
# file3='./data/P01_01.npz'

# tsp_feature=np.load(file1)
# print(tsp_feature.shape)
# i3d_feature=np.load(file2)
# print(i3d_feature.shape)
# i3d_feature_1=np.load(file2_1)
# print(i3d_feature_1.shape)
# feature=np.load(file3)
# print(feature.files)
# feats=feature['feats']
# print(feats.shape)

# file= '../feature_extract/20220628001-rgb.npz'
# feature=np.load(file)
# print(feature['feature'].shape)

# with open('data/jump/annotations/Jump_label.json', 'r') as fid:
#     json_data = json.load(fid)
# json_db = json_data['database']
# print(len(json_db))


def read_pickle(work_path):
    data_list = []
    with open(work_path, "rb") as f:
        while True:
            try:
                data = pickle.load(f)
                data_list.append(data)
            except EOFError:
                break
    return data_list



