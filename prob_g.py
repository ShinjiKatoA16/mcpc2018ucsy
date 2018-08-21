#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def solve(s):
    open_p = ('[', '{', '(')
    close_p = (']', '}', ')')
    pair = dict(zip(close_p, open_p))  # key: close_p

    stack = list()
    for c in s:
        if c in open_p:
            stack.append(c)
        if c in close_p:
            if len(stack) == 0:
                print('NO')
                return
            top = stack.pop()
            if top != pair[c]:
                print('NO')
                return
    if len(stack) != 0:
        print('NO')
        return
    print('YES')
    return

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    s = sys.stdin.readline().strip()
    solve(s)
