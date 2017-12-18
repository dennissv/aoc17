#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:42:53 2017

@author: dennis
"""

wall = {}
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = [int(x) for x in line.strip('\n').split(': ')]
        wall[line[0]] = (line[1]-1)*2

delay = -1
caught = True
while caught:
    delay += 1
    caught = False
    for x in wall:
        if ((delay+x) % wall[x]) == 0:
            caught = True
            break
print(delay)