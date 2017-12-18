#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 05:51:03 2017

@author: dennis
"""

import operator

ops = {'>': operator.gt,
       '<': operator.lt,
       '<=': operator.le,
       '>=': operator.ge,
       '==': operator.eq,
       '!=': operator.ne}

lines = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n').split()
        lines.append(line)
    
reg = {}    
for i in lines:
    if i[0] not in reg:
        reg[i[0]] = 0

max_ = 0
for i in lines:
    if ops[i[5]](reg[i[4]],int(i[6])):
        if i[1] == 'dec':
            reg[i[0]] -= int(i[2])
        else:
            reg[i[0]] += int(i[2])
    if max(reg.values()) > max_:
        max_ = max(reg.values())
print(max(reg.values()))
print(max_)