import os
import sys
import subprocess


def process_video(root_dir='../video', save_dir='../test'):
    files = os.listdir(root_dir)
    for video_filename in files:
        video_filename = video_filename.split('.')[0]
        video = os.path.join(root_dir, video_filename + '.mkv')
        dst_path= os.path.join(save_dir, video_filename)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        cmd = 'ffmpeg -i \"{}\" -r 1 -q:v 2 -f image2 \"{}/%03d.jpg\"'.format(video, dst_path)
        subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print('{} has finished'.format(video_filename))

process_video()