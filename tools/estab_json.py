import numpy as np
import json
import os
import torch
import csv
import pandas as pd


def load_label():
    file = pd.read_csv('../data/jump/annotations/Jump_label.csv', header=0)
    label_dict = {}
    label_dict["version"] = "LongJump6.28"
    label_dict["database"] = {}
    for i in range(len(file)):
        if file.iloc[i, 1] != 'None' and file.iloc[i, 2] != 'None':
            label_dict['database'][str(file.iloc[i, 0])] = {}
            label_dict['database'][str(file.iloc[i, 0])]["annotations"] = []
            label_dict['database'][str(file.iloc[i, 0])]["annotations"].append(
                {"label": "0", "label_id": 0, "segment": [float(file.iloc[i, 1])/30.0, float(file.iloc[i, 2])/30.0]})
            random_num = np.random.rand(1)
            if random_num < 0.8:
                label_dict['database'][str(file.iloc[i, 0])]['subset'] = "training"
            else:
                label_dict['database'][str(file.iloc[i, 0])]['subset'] = "validation"
            label_dict['database'][str(file.iloc[i, 0])]['duration'] = int(file.iloc[i, 2]) - int(file.iloc[i, 1])
            label_dict['database'][str(file.iloc[i, 0])]['fps'] = 30

    return label_dict


label_dict = load_label()
for k, v in label_dict['database'].items():
    print(k, v)
with open('../data/jump/annotations/Jump_label1.json', 'w') as fid:
    json.dump(label_dict, fid)
