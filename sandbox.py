import heapq
import time
import random, pprint


def astar(maze, start, end):
    hqueue = [start]
    visited = {(0,0):0}
    parent = {}
    heapq.heapify(hqueue)

    while hqueue:
        distance, cost, x, y = heapq.heappop(hqueue)
        neighbors = get_neighbors(maze,x,y)

        for cx, cy in neighbors:
            if ((cx,cy) not in visited) or( cost + maze[cx][cy] < visited[(cx,cy)]):
                visited[(cx,cy)] = cost
                new_distance = abs(end[0]-cx) - abs(end[1]-cy)
                heapq.heappush(hqueue, (new_distance, cost+maze[cx][cy], cx, cy))
                parent[(cx,cy)] = (x,y)

                if (cx,cy) == end:
                    print('Found')
                    return (visited[end], parent)


def get_neighbors(maze, x, y):
    neighbors = ((x+1, y), (x-1,y), (x, y-1), (x, y+1), (x+1, y-1), (x-1, y-1), (x+1,y+1), (x-1,y+1))
    real_neighbors = ((x,y) for x,y in neighbors if 0<= x < len(maze) and 0<= y < len(maze[0]))
    return real_neighbors


if __name__ == "__main__":
    matrix = [[random.randint(0,10) for x in range(20)]for y in range(20)]
    start_time = time.time()

    length = len(matrix)-1
    total, parent = astar(matrix, (0,0,0,0), (length,length))
    print("Ran in %s seconds ---" % (time.time() - start_time))
    print('cost is', total)
    currentNode = (length,length)
    while currentNode != (0,0):
        x,y = currentNode
        matrix[x][y] = "X"
        currentNode = parent[(x,y)]
    matrix[0][0] = 'X'
    pprint.pprint(matrix)
