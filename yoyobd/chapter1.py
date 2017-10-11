#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'


import numpy as np
import os
from collections import defaultdict

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# print(BASE_PATH)
data_file = os.path.join(BASE_PATH, 'data/affinity_dataset.txt').replace('/', '\\')
# print(data_file)

X = np.loadtxt(data_file)
n_samples, n_features = X.shape
# print(X.shape)

features = ['bread', 'milk', 'cheese', 'apples', 'bananas']

valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurances = defaultdict(int)

for sample in X:
    for premise in range(n_features):
        if sample[premise] == 0:
            continue
        num_occurances[premise] += 1
        for conclusion in range(n_features):
            if premise == conclusion:
                continue
            if sample[conclusion] == 1:
                valid_rules[(premise, conclusion)] += 1
            else:
                invalid_rules[(premise, conclusion)] += 1


support = valid_rules   #支持度
confidence = defaultdict(float) #置信度

for premise, conclusion in valid_rules.keys():
    rule = (premise, conclusion)
    confidence[rule] = valid_rules[rule] / num_occurances[premise]

print(confidence)

print(type(valid_rules))
print(valid_rules)
print(type(invalid_rules))
print(invalid_rules)