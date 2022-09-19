import numpy as np
import os

file_path = 'E:\Project\Sit_and_reach_mp4'
file_list = os.listdir(file_path)
print(file_list)
video_list = []
for file in file_list:
    video_path = os.path.join(file_path, file)
    video_list.append(video_path)
print(video_list)
with open('feature_extract__mmaction2/video_list.txt', 'w') as fid:
    for video in video_list:
        fid.write(video + '\n')
