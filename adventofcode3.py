#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:18:31 2017

@author: dennis
"""

#First part solved mathematically

import numpy as np

def sum_neighbours(pos):
    return sum(mat[pos[0]-1][pos[1]-1:pos[1]+2])+sum(mat[pos[0]+1][pos[1]-1:pos[1]+2])+mat[pos[0]][pos[1]-1]+mat[pos[0]][pos[1]+1]

mat = np.zeros((11,11))
mat[5,5] = 1
position = np.array([5,5])
direction = 0
directions = [np.array([0,1]), np.array([-1,0]), np.array([0,-1]), np.array([1,0])]
changes = [i for i in range(1,11) for j in range(2)] #Keeps track of how often to change direction
changes_inrow = 0
changes_pos = 0

n = 1
while n < 368078:
    position += directions[direction]
    n = sum_neighbours(position)
    mat[position[0]][position[1]] = n
    changes_inrow += 1
    if changes_inrow >= changes[changes_pos]:
        direction = (direction+1) % 4
        changes_inrow = 0
        changes_pos += 1
print(int(mat.max()))