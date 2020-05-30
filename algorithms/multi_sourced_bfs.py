import random, pprint, heapq
matrix = [[random.randint(0,2) for _ in range(5)] for _ in range(5)]

def multiBFS(graph):
    queue = []
    timey = 0
    n = len(graph)
    m = len(graph[0])
    fresh = {}

    # init fresh and queue
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j,0))
            elif graph[i][j] == 1:
                fresh[(i,j)] = 1

    while queue:
        node = queue.pop(0)
        x,y,turn = node 
        for cx,cy in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if 0 <= cx < n and 0 <= cy < m:
                if graph[cx][cy] == 1:
                    fresh.pop((cx,cy), None)
                    queue.append((cx,cy,turn+1))
                    graph[cx][cy] = 2
    return -1 if len(fresh) > 0 else turn


def rotten_oranges(graph):
    fresh = {}
    queue = []
    n = len(graph)
    m = len(graph[0])

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j,0))
            elif graph[i][j] == 1:
                fresh[(i,j)] = 1
    
    directions = ((0,1), (1,0), (-1,0),(0,-1))
    while queue:
        x,y,lvl = queue.pop(0)
        for edge in directions:
            cx = x+edge[0]
            cy = y+edge[1]
            if 0<= cx < n and 0<= cy <m:
                if graph[cx][cy] == 1:
                    queue.append((cx,cy,lvl+1))
                    fresh.pop((cx,cy), None)
                    graph[cx][cy] = 2
        
    return -1 if len(fresh) > 0 else lvl

import copy
# graph = copy.deepcopy(matrix)
# pprint.pprint(matrix)    
#print(multiBFS(graph))
print(rotten_oranges(matrix))
pprint.pprint(matrix)    
