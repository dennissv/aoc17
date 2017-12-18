#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:55:11 2017

@author: dennis
"""

import itertools

summa = 0
invalids = 0
with open('input4.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n').split(' ')
        summa += 1
        for word in line:
            t_line = line[:line.index(word)] + line[line.index(word)+1:]
            for combo in itertools.permutations(word, len(word)):
                combo_c = ''
                for l in combo:
                    combo_c += l
                if t_line.count(combo_c) != 0:
                    invalids += 1
                    break
            else:
                continue
            break

print(summa-invalids)