#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

RIGHT = 1
DOWN = 2
BOTH = RIGHT+DOWN
BIG_NUM = 10**9+7

def solve(maze, m_size):
    num_path = [[0 for col in range(m_size)] for row in range(m_size)]
    value = maze.copy()

    num_path[m_size-1][m_size-1] = 1

    for row in range(m_size-1, -1, -1):
        for col in range(m_size-1, -1, -1):
            if row == m_size - 1 and col == m_size -1: continue
            if col != m_size - 1 and maze[row][col] & RIGHT:
                num_path[row][col] += num_path[row][col+1]
            if row != m_size - 1 and maze[row][col] & DOWN:
                num_path[row][col] += num_path[row+1][col]
            if num_path[row][col] == 0:
                value[row][col] = 0
            elif maze[row][col] == RIGHT:
                value[row][col] += value[row][col+1]
            elif maze[row][col] == DOWN:
                value[row][col] += value[row+1][col]
            elif maze[row][col] == BOTH:
                if col == m_size-1:
                    value[row][col] += value[row+1][col]
                elif row == m_size-1:
                    value[row][col] += value[row][col+1]
                else:
                    value[row][col] += max(value[row][col+1], value[row+1][col])
            else:
                raise

    #print('num_path:', num_path, file=sys.stderr)
    #print('value:', value, file=sys.stderr)

    print(num_path[0][0] % BIG_NUM, value[0][0] % BIG_NUM)


num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    m_size = int(sys.stdin.readline())
    maze = list()
    for i in range(m_size):
        maze.append(list(map(int,sys.stdin.readline().split())))

    solve(maze, m_size)
