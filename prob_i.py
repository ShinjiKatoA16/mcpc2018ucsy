#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def my_int(st):
    return 0 if st == '' else int(st)

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    s = sys.stdin.readline().strip()  # remove \n
    nums = list(map(my_int,s.split(',')))
    val = 0
    for n in nums:
        val = val*60 + n
    print(val)
