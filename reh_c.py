#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
MCPC 2018: Rehearsal Problem C: Traversal
'''

import sys


def post_order(pre_o, in_o):
    '''
    pre_o: String
    in_o: String
    return List of single string
    '''

    po = list()   # list of post_order

    root = pre_o[0]
    left_len = in_o.index(root)
    right_len = len(pre_o) - (left_len + 1)

    if left_len:
        left_pre_o = pre_o[1:left_len+1]  # Not include root
        left_in_o = in_o[:left_len]  # Not include root
        po.extend(post_order(left_pre_o, left_in_o))

    if right_len:
        right_pre_o = pre_o[left_len+1:]  # Not include root
        right_in_o = in_o[left_len+1:]  # Not include root
        po.extend(post_order(right_pre_o, right_in_o))

    po.append(root)   # Add root
    return po


num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    l_str, pre_o, in_o = sys.stdin.readline().split()
    po = post_order(pre_o, in_o)
    print(''.join(po))
