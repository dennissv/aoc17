#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:42:53 2017

@author: dennis
"""

with open('input.txt','r') as f:
    for line in f.readlines():
        inp = line.strip('\n')

scores = []
c = 0
garbage = False
canceled = False
score = 0
g_score = 0
#inp = '<<<<>'
gc = False
while c < len(inp):
    if inp[c] == '!':
        c += 1
        canceled = True
    elif (inp[c] == '<') and (not garbage):
        garbage = True
        gc = True
    elif (inp[c] == '>'):
        garbage = False
    elif (inp[c] == '{') and (not garbage):
        score += 1
        scores.append(score)
    elif (inp[c] == '}') and (not garbage):
        score -= 1
    if (garbage) and (not canceled) and (not gc):
        g_score += 1
    c += 1
    canceled = False
    gc = False
print(sum(scores))
print(g_score)