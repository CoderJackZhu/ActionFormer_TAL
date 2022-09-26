import numpy as np
import json
import os
import torch
import csv
import pandas as pd


# for file in files:
#     label_dict['database'][file] = {}
#     label_dict['database'][file]["annotations"] = []
#     label_dict['database'][file]['subset'] = "test"
#     label_dict['database'][file]['duration'] = duration
#     label_dict['database'][file]['fps'] = fps

def load_label(videos_dict):
    label_dict = {}
    label_dict["version"] = "SitReachTest"
    label_dict["database"] = {}
    for k, v in videos_dict.items():
        label_dict['database'][k] = {}
        for k1, v1 in v.items():
            label_dict['database'][k][k1] = v1
        label_dict['database'][k]['subset'] = "test"
    return label_dict

def make_test_json(label_dict, json_file='./test_set.json'):
    label_dict = load_label(label_dict)
    for k, v in label_dict['database'].items():
        print(k, v)
    with open(json_file, 'w') as fid:
        json.dump(label_dict, fid)
if __name__ == '__main__':
    label_dict = {'001.mp4': {'duration': 10.0, 'fps': 30}, '002.mp4': {'duration': 10.0, 'fps': 30}}
    make_test_json(label_dict)


