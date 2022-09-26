import os.path
import numpy as np
import json
import pickle


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


def get_sit_frame(pkl_path='./models/sit_best_ckpt/sit_i3d_reproduce/eval_results.pkl', fps=30.0):
    data_list = read_pickle(pkl_path)
    data_list = data_list[0]
    video_id = data_list['video-id']
    t_end = data_list['t-end']
    score = data_list['score']
    id_list = []
    result_list = []
    for i in range(len(video_id)):
        # print(video_id[i], t_end[i], score[i])
        if video_id[i] not in id_list:
            id_list.append(video_id[i])
            result_list.append([video_id[i], t_end[i]])
        else:
            continue

    return result_list


if __name__ == '__main__':
    result_list = get_sit_frame(pkl_path='./models/sit_best_ckpt/sit_i3d_reproduce/eval_results.pkl', fps=30.0)
    print(result_list)
