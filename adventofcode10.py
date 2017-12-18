#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:42:53 2017

@author: dennis
"""

from functools import reduce

inpo = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'
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
print(hexed)