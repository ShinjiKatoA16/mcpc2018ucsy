#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
MCPC 2018: Problem C: Pattern Matching
'''

import sys

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    subs = sys.stdin.readline().strip()
    s = sys.stdin.readline().strip()
    found = 0
    f_pos = list()
    p_idx = -1
    while True:
        # print(p_idx, subs, s)
        p_idx = s.find(subs, p_idx+1)
        if p_idx == -1:
            break
        found += 1
        f_pos.append(str(p_idx))
    print(found)
    print(' '.join(f_pos))
