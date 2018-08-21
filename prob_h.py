#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
MCPC 2018 Problem-H: Gold Mining
'''

import sys


def check_mines(mines, p1, p2):
    '''
    mines: list of tuple (x1, x2, y)
    p1, p2: tuple (x,y)
    return: total length of mines on the p1-p2 line
    '''

    total_len = 0
    slope_p1_p2 = (p2[0]-p1[0]) / (p2[1]-p1[1])
    for mine in mines:
        mine_x = (slope_p1_p2 * (mine[2]-p1[1])) + p1[0]
        #print(p1, p2, slope_p1_p2, mine, mine_x, file=sys.stderr)
        if mine_x >= mine[0] and mine_x <= mine[1]:
            total_len += mine[1]-mine[0]

    return total_len


def solve(mines):
    points = list()
    for mine in mines:
        points.append((mine[0],mine[2]))  # (x1, y)
        points.append((mine[1],mine[2]))  # (x2, y)

    max_total = 0
    for p1_idx in range(len(points)-1):
        for p2_idx in range(p1_idx, len(points)):
            if points[p1_idx][1] == points[p2_idx][1]: continue  # same y
            total_len = check_mines(mines, points[p1_idx], points[p2_idx])
            max_total = max(max_total, total_len)

    print('{:.2f}'.format(round(max_total/3,2)))


num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    num_mine = int(sys.stdin.readline())
    mines = list()
    for m in range(num_mine):
        x1, x2, y = map(int, sys.stdin.readline().split())
        mines.append((x1, x2, y))

    solve(mines)
