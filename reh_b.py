#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MCPC 2018 Rehearsal Problem B: Right Triangle

import sys

def right_triangle(edges):
    max_edge = max(edges)
    edges.remove(max_edge)
    if max_edge**2 == edges[0]**2 + edges[1]**2:
        return 1
    else:
        return 0

num_tc = int(sys.stdin.readline())
for tc in range(num_tc):
    edges = list(map(int, sys.stdin.readline().split()))
    print(right_triangle(edges))
