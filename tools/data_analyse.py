import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


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
            result_list.append([video_id[i], t_end[i]*fps])
        else:
            continue

    return result_list

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


def analyse_frame(data_path='../ckpt/sit_reproduce/eval_results.pkl'):
    results=get_sit_frame(pkl_path=data_path)
    data = pd.DataFrame(results)
    file = pd.read_csv('F:/Code/PE project/sit_reach_mmpose/pose/src/source_data.csv', header=0)
    assert len(file) == len(data)
    frame_abs_error_list, frame_rel_error_list = [], []
    for i in range(file.shape[0]):
        print(data.iloc[i,1], file.iloc[i,3])
        frame_abs_error = round(data.iloc[i, 1]) - file.iloc[i, 3]
        frame_rel_error = frame_abs_error / file.iloc[i, 3]
        frame_abs_error_list.append(frame_abs_error)
        frame_rel_error_list.append(frame_rel_error)

    frame_average_error = sum(map(abs, frame_abs_error_list)) / len(frame_abs_error_list)
    print('预测帧平均误差为{:.2f}'.format(frame_average_error))
    plt.hist(frame_abs_error_list)
    plt.title('frame_absolute_error')
    plt.show()
    plt.hist(frame_rel_error_list)
    plt.title('frame_relative_error')
    plt.show()
    fig1, axes = plt.subplots()
    sns.boxplot(data=frame_abs_error_list, orient='v', ax=axes)
    plt.title('frame_absolute_error boxplot')
    plt.show()


if __name__ == '__main__':
    analyse_frame()
