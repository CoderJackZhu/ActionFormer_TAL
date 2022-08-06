import numpy as np



file1='./data/v___c8enCfzqw.npy'
file2='./data/video_test_0000004.npy'
file2_1='./data/video_test_0000006.npy'
file3='./data/P01_01.npz'

tsp_feature=np.load(file1)
print(tsp_feature.shape)
i3d_feature=np.load(file2)
print(i3d_feature.shape)
i3d_feature_1=np.load(file2_1)
print(i3d_feature_1.shape)
feature=np.load(file3)
print(feature.files)
feats=feature['feats']
print(feats.shape)