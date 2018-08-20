#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
MCPC 2018 Problem-A: Taxi Driver
'''

import sys
from heapq import heappush, heappop
from collections import defaultdict

INF = 10**18
DEFAULT_EDGE = 10


def init_edges(min_x, max_x, min_y, max_y, jams):
    edges = dict()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            left = None if x == min_x else DEFAULT_EDGE
            right = None if x == max_x else DEFAULT_EDGE
            down = None if y == min_y else DEFAULT_EDGE
            up = None if y == max_y else DEFAULT_EDGE
            edges[(x,y)] = [right, left, up, down]

    for jam in jams:
        for y in range(jam[1]+1, jam[3]):  # exclude y1, y2
            for x in range(jam[0], jam[2]):  # include x1, exclude x2
                edges[(x,y)][0] = jam[4]
                edges[(x+1,y)][1] = jam[4]

        for x in range(jam[0]+1, jam[2]):  # exclude x1, x2
            for y in range(jam[1], jam[3]):  # include y1, exclude y2
                edges[(x,y)][2] = jam[4]
                edges[(x,y+1)][3] = jam[4]

    # print(edges)
    return edges


def eval_node(node, weight, pq, distance ,temp_dist, edges):
    #print('Node:', node, 'evaluated', weight, file=sys.stderr)
    temp_dist[node] = distance[node] = weight

    right, left, up, down = edges[node]
    x, y = node

    if right != None:
        next_node = (x+1, y)
        new_weight = weight + right
        if new_weight < temp_dist[next_node]:
            heappush(pq, (new_weight, next_node))
            temp_dist[next_node] = new_weight

    if left != None:
        next_node = (x-1, y)
        new_weight = weight + left 
        if new_weight < temp_dist[next_node]:
            heappush(pq, (new_weight, next_node))
            temp_dist[next_node] = new_weight

    if up != None:
        next_node = (x, y+1)
        new_weight = weight + up
        if new_weight < temp_dist[next_node]:
            heappush(pq, (new_weight, next_node))
            temp_dist[next_node] = new_weight

    if down != None:
        next_node = (x, y-1)
        new_weight = weight + down
        if new_weight < temp_dist[next_node]:
            heappush(pq, (new_weight, next_node))
            temp_dist[next_node] = new_weight
    

def dijkstra(src, dest, edges):
    '''
    src: tuple (x,y)
    dest: tuple (x,y)
    edges: dictionary  key: (x,y) value: [right, left, up, down]
    '''

    distance = defaultdict(lambda: INF) # distance from src
    distance[src] = 0

    temp_dist = distance.copy()  # minimum distance in queue

    pq = list()   # priority queue
    eval_node(src, 0, pq, distance, temp_dist, edges)

    while pq:
        weight, node = heappop(pq)
        if node == dest:
            print(weight)
            return
        eval_node(node, weight, pq, distance, temp_dist, edges)

    print('path to dest not found')

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    src_x, src_y, dist_x, dist_y = map(int, sys.stdin.readline().split())
    min_x = min(src_x, dist_x)
    max_x = max(src_x, dist_x)
    min_y = min(src_y, dist_y)
    max_y = max(src_y, dist_y)
    
    num_jam = int(sys.stdin.readline())
    jams = list()
    for j in range(num_jam):
        x1, y1, x2, y2, t = map(int, sys.stdin.readline().split())
        jams.append((x1, y1, x2, y2, t))
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)

    edges = init_edges(min_x, max_x, min_y, max_y, jams)
    dijkstra((src_x, src_y), (dist_x, dist_y), edges)

