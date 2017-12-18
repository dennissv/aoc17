#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:42:53 2017

@author: dennis
"""

from functools import reduce
    
def knot(inpo):
    inp = [ord(x) for x in inpo] + [17, 31, 73, 47, 23]
    li = [x for x in range(256)]
    
    cpos, skip = 0, 0
    for _ in range(64):
        for length in inp:
            leftover = max((cpos + length), 256) % len(li)
            current = li[cpos:min(len(li), cpos + length)] + li[:leftover]
            current.reverse()
            if leftover:
                li = current[-leftover:] + li[leftover:cpos] + current[:-leftover]
            else:
                li = li[:cpos] + current + li[cpos+length:]
            cpos = (cpos + length + skip) % len(li)
            skip += 1
    
    dense = [reduce(lambda x, y: x ^ y, li[i*16:i*16+16]) for i in range(16)]
    hexed = ''.join(f'{n:02x}' for n in dense)
    return hexed
    
def neigh(p):
    n = []
    if p[0]: n.append((p[0]-1,p[1]))
    if p[1]: n.append((p[0],p[1]-1))
    if p[0] < 127: n.append((p[0]+1,p[1]))
    if p[1] < 127: n.append((p[0],p[1]+1))
    return n
        
t = 'uugsqrei'

grid = [[] for x in range(128)]
s = 0
for i in range(128):
    key = t+'-'+str(i)
    binary = bin(int(knot(key), 16))[2:]
    for l in binary:
        if l == '1':
            s += 1
    pad = 128-len(binary)
    binary = '0'*pad+binary
    grid[i] = binary
print('Part 1: %d' % s)

cr = 1
regions = [[-1]*128 for x in range(128)]
explored = set()
for i in range(128):
    for j in range(128):
        c = (i,j)
        if (grid[c[0]][c[1]] == '1') and (not c in explored):
            to_explore = [c]
            while to_explore:
                for x in to_explore:
                    if (grid[x[0]][x[1]] == '1') and (x not in explored):
                        regions[x[0]][x[1]] = cr
                        explored.add(x)
                        cn = neigh(x)
                    for c_ in cn:
                        if (grid[c_[0]][c_[1]] == '1') and (c_ not in explored):
                            regions[c_[0]][c_[1]] = cr
                            explored.add(c_)
                            to_explore += neigh(c_)
                    to_explore.remove(x)
            cr += 1

m = 0
for reg in regions:
    for r in reg:
        if r > m:
            m = r
print('Part 2: %d' % m)