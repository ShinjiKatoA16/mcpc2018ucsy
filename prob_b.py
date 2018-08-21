#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

MAX_N = 1000
def sieve():
    primes = list()
    perfects = list()
    others = list()
    PRIME = 1
    PERFECT = 2
    OTHER = 0

    p_num = [PRIME for i in range(MAX_N)]
    p_num[0] = p_num[1] = OTHER 

    for n in range(2, MAX_N):
        if p_num[n] == PRIME:
            primes.append(n)
            for mop in range(n*2, MAX_N, n):
                p_num[mop] = OTHER 

    for n in range(2, MAX_N):
        if n*n < MAX_N:
            perfects.append(n*n)
            p_num[n*n] = PERFECT
        if p_num[n] == OTHER:
            others.append(n)


    #print('Prime:', primes)
    #print('Pefects:', perfects)
    #print('Others:', others)
    return primes, perfects, others


primes, perfects, others = sieve()

num_tc = int(sys.stdin.readline())
for tc in range(num_tc):
    prime_idx = perfect_idx = other_idx = 0
    s = sys.stdin.readline().strip()  # remove \n
    print('Case {}:'.format(tc+1), end=' ')

    out_s = list()
    for c in s:
        c_bin = bin(ord(c))[2:]
        c_bin = '00000000'[:8-len(c_bin)] + c_bin
        for pos in range(0,8,2):  # 8bit / 2
            if c_bin[pos:pos+2] == '00':
                out_s.append(str(perfects[perfect_idx]))
                perfect_idx += 1
            elif c_bin[pos:pos+2] == '11':
                out_s.append(str(primes[prime_idx]))
                prime_idx += 1
            else:
                out_s.append(str(others[other_idx]))
                other_idx += 1

    print(','.join(out_s))
