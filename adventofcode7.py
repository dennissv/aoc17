#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 02:09:33 2017

@author: dennis
"""

programs = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n').replace(',','')
        programs.append(line)

actual = []
for program in programs:
    actual.append(program.split()[0])

for program in programs:
    if '->' not in program:
        try:
            actual.remove(program.split()[0])
        except:
            None
    for w in program.split()[3:]:
        try:
            actual.remove(w.strip(','))
        except:
            None
            
print(actual[0])

weights = {}
while len(programs) > len(weights):
    for program in programs:
        program = program.split()
        if len(program) == 2:
            weights[program[0]] = int(program[1][1:-1])
        if len(program) > 2:
            condition = True
            for aprogram in program[3:]:
                if aprogram not in weights:
                    condition = False
            if condition:
                cweight = int(program[1][1:-1])
                for cprogram in program[3:]:
                    cweight += weights[cprogram]
                weights[program[0]] = cweight

c = 0
for program in programs:
    wat = program
    program = program.split()[3:]
    if len(program) > 0:
        tweight = 0
        for aprogram in program:
            tweight += weights[aprogram]
        if (tweight % len(program)) != 0:
            for tmp in program:
                print(weights[tmp])
            break
    c += 1