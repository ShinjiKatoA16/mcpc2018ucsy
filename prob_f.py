#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

symmetry = {'A':1, 'B':1, 'C':1, 'D':1, 'E':1, 'F':0, 'G':0,
            'H':2, 'I':2, 'J':0, 'K':0, 'L':0, 'M':1, 'N':0,
            'O':2, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':1, 'U':1,
            'V':1, 'W':1, 'X':2, 'Y':1, 'Z':0}


def value(s):
    worth = 0
    for c in s:
        if c in symmetry:
            worth += symmetry[c]
    return worth

tc_num = 0
while True:
    num_str = int(sys.stdin.readline())
    if num_str == 0:
        break
    tc_num += 1
    print('Case {}:'.format(tc_num))
    for i in range(num_str):
        s = sys.stdin.readline().strip()
        print(s, value(s))
