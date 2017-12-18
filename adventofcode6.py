#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 05:53:35 2017

@author: dennis
"""

#import itertools

with open('input.txt', 'r') as f:
    for line in f.readlines():
        blocks = [int(x) for x in line.strip('\n').split('\t')]

states = []
tested = 1
while True:
    highest = max(blocks)
    start = blocks.index(highest)
    blocks[start] = 0
    for i in range(start+1,highest+start+1):
        blocks[i%len(blocks)] += 1
    state = [x for x in blocks]
    if state in states:
        break
    states.append(state)
    tested += 1
    
state_tofind = state
new = 1
while True:
    highest = max(blocks)
    start = blocks.index(highest)
    blocks[start] = 0
    for i in range(start+1,highest+start+1):
        blocks[i%len(blocks)] += 1
    state = [x for x in blocks]
    if state == state_tofind:
        break
    states.append(state)
    new += 1
print(new)