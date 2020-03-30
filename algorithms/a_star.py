import heapq
import time,random


def path_finder(matrix):

    length = len(matrix)
    start = (0,0,0,0)
    goal = (length-1, length-1)

    parent = {}
    visited = {(0,0): 0}
    unseenNodes = [start]
    heapq.heapify(unseenNodes)

    while unseenNodes:
        minNode = heapq.heappop(unseenNodes)
        #unseenNodes = sorted(unseenNodes, key = lambda x: x[3])
        #minNode = unseenNodes.pop(0)

        distance, current_weight, x, y = minNode
        px, py = x,y

        neighbors = ((x-1,y),(x,y-1),(x+1,y),(x,y+1), (x-1,y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1))
        real_neighbors = ((x,y) for (x,y) in neighbors if 0 <= x < length and 0<= y < length)

        for cx,cy in real_neighbors:
            cost = current_weight + matrix[cx][cy]
            dist = abs(goal[0] - cx) + abs(goal[1]-cy)
            if (cx,cy) not in parent or cost < visited[(cx,cy)]:
                visited[(cx,cy)] = cost
                heapq.heappush(unseenNodes,(dist,cost,cx,cy))
                #unseenNodes.append((ccost,cost,cx,cy))
                parent[(cx,cy)] = (px,py)

                if (cx,cy) == goal:
                    print('hey, hey, hey')

                    # currentNode = (length-1,length-1)
                    # while currentNode != (0,0):
                    #     x,y = currentNode
                    #     matrix[x][y] = "X"
                    #     currentNode = parent[(x,y)]
                    # matrix[0][0] = 'X'
                    return (visited[goal])


import random, pprint
matrix = [[x + 1 for x in range(100)] for y in range(100)]
start_time = time.time()
print(path_finder(matrix))
print("--- %s seconds ---" % (time.time() - start_time))
