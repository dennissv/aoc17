#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:42:53 2017

@author: dennis
"""

def distance(m_):
    m = m_.copy()
    for i in range(4):
        c, n2, nm2 = m[i], m[i+2], m[(i-2)%6]
        if c >= n2:
            m[i+2] -= n2
        elif c < nm2:
            m[i] -= c
        if c >= nm2:
            m[(i-2)%6] -= nm2
        elif c < nm2:
            m[i] -= c
    return sum(m)

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n').split(',')
        
cmap = ['n', 'ne', 'se', 's', 'sw', 'nw']
ops = {'s': 'n', 'se': 'nw', 'ne': 'sw', 'n': 's', 'nw': 'se', 'sw': 'ne'}
moves = [0 for x in range(6)]
max_dist = 0
for ins in line:
    if (moves[cmap.index(ops[ins])] > 0):
        moves[cmap.index(ops[ins])] -= 1
    else:
        moves[cmap.index(ins)] += 1
    if distance(moves) > max_dist:
        max_dist = distance(moves)
print('Part 1: %d' % distance(moves))
print('Part 2: %d' % max_dist)