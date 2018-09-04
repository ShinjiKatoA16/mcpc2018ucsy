#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MCPC 2018 Rehearsal Problem-A: Arm-Strong Number


import sys

def arm_strong(n):
    total = 0
    numbers = map(int, list(str(n)))
    for digit in numbers:
        total += digit**3

    return(1 if total==n else 0)


num_tc = int(sys.stdin.readline())
for tc in range(num_tc):
    n = int(sys.stdin.readline())
    print(arm_strong(n))

