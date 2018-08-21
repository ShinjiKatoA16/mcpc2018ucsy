#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
MCPC 2018: Problem D: Round Robin Tournament
'''

import sys

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    team, guess = map(int, sys.stdin.readline().split())
    match = team*(team-1)//2  # nC2
    if match == guess:
        print('CORRECT')
    else:
        print('INCORRECT', match)

