import mmcv
import csv
import pandas as pd
import os

video_path='E:/Project/Sit_and_reach_mp4'
video_list = os.listdir(video_path)
video_list.sort()
video_list = [os.path.join(video_path, video) for video in video_list]
video_frames=[]
for video in video_list:
    video = mmcv.VideoReader(video)
    video_frames.append(video.frame_cnt)
video_frames=pd.DataFrame(video_frames)
video_frames.to_csv('video_frames.csv',index=False,header=False)