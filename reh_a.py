#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MCPC 2018 Rehearsal Problem-A: Arm-Strong Number


import sys

def arm_strong(n):
    total = 0
    number = n
    while number>0:
        digit = number % 10
        total += digit**3
        number //= 10

    if (total == n):
        return 1
    else:
        return 0


num_tc = int(sys.stdin.readline())
for tc in range(num_tc):
    n = int(sys.stdin.readline())
    print(arm_strong(n))

