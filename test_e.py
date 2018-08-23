#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randrange

N= 1000  # size of Matrix

print(1)
print(N)

for _ in range(N):
    x = [str(randrange(3)+1) for i in range(N)]
    print(' '.join(x))
