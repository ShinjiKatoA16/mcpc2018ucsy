#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MCPC 2018 Rehearsal Problem-A: Arm-Strong Number


import sys

def arm_strong(s):
    total = 0
    numbers = map(int, s)   # map() will apply int() to each digit in s
    for digit in numbers:
        total += digit**3

    return(1 if total==int(s) else 0)


num_tc = int(sys.stdin.readline())
for tc in range(num_tc):
    s = sys.stdin.readline().strip()  # pass as string, remove \n
    print(arm_strong(s))

