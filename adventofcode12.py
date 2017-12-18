#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:42:53 2017

@author: dennis
"""

import networkx as nx

g = nx.Graph()

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n').split('<-> ')
        id_ = int(line[0])
        edges = [int(x) for x in line[1].split(', ')]
        for e in edges:
            g.add_edge(id_,e)

print('Part 1: %d' % len(nx.node_connected_component(g, 0)))
print('Part 2: %d' % len(list(nx.connected_component_subgraphs(g))))