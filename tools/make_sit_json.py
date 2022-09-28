import numpy as np
import json
import os
import torch
import csv
import pandas as pd


def load_label():
    fps=30.0
    file = pd.read_csv('../data/sit/annotations/source_data.csv', header=0)
    label_dict = {}
    label_dict["version"] = "SitReach6.28"
    label_dict["database"] = {}
    for i in range(len(file)):
        if file.iloc[i, 3] != 'None' and file.iloc[i, 4] != 'None':
            label_dict['database'][str(file.iloc[i, 0])] = {}
            label_dict['database'][str(file.iloc[i, 0])]["annotations"] = []
            label_dict['database'][str(file.iloc[i, 0])]["annotations"].append(
                {"label": "0", "label_id": 0, "segment": [float(0), float(file.iloc[i, 3])/fps]})
            random_num = np.random.rand(1)
            if random_num < 0.8:
                label_dict['database'][str(file.iloc[i, 0])]['subset'] = "training"
            else:
                label_dict['database'][str(file.iloc[i, 0])]['subset'] = "validation"
            label_dict['database'][str(file.iloc[i, 0])]['duration'] = (float(file.iloc[i, 7]))/fps
            label_dict['database'][str(file.iloc[i, 0])]['fps'] = 30.0

    return label_dict


label_dict = load_label()
for k, v in label_dict['database'].items():
    print(k, v)
with open('../data/sit/annotations/Sit_label.json', 'w') as fid:
    json.dump(label_dict, fid)
