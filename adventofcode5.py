#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 01:39:49 2017

@author: dennis
"""

maze = []
with open('input5.txt', 'r') as f:
    for line in f.readlines():
        maze.append(int(line.strip('\n')))
        
moves = 0
pos = 0
old_pos = 0

while 1:
    try:
        pos += maze[pos]
        moves += 1
        if maze[old_pos] >= 3:
            maze[old_pos] -= 1
        else:
            maze[old_pos] += 1
        old_pos = pos
    except:
        print(moves)
        break