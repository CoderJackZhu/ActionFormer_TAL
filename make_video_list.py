import numpy as np
import os

file_path='E:\Project\Long_jump'
file_list=os.listdir(file_path)
video_list=[]
for file in file_list:
    file_path=os.path.join(file_path,file)
    video_list.append(file_path)

with open('./video_list.txt','w') as fid:
    for video in video_list:
        fid.write(video+'\n')
