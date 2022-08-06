import numpy as np
import json
import os
import torch
import csv
import pandas as pd


def load_label():
    label_dict = {}
    with open('./data/label.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            label_dict[row[0]] = int(row[1])
    return label_dict
# def load_labe