'''
This problem was asked by Uber.

You are given a 2-d matrix where each cell consists of either /, \
or an empty space. Write an algorithm that determines into how many
regions the slashes divide the space.

For example, suppose the input for a three-by-six grid is the following:

\    /
 \  /
  \/

'''
grid = [
        ["%"," "," "," "," ","/"],
        [" ","%"," "," ","/"," "],
        [" "," ","%","/"," "," "]
        ]
print(grid)
def grid_regions(matrix):
    regions = 0
    best = 0
    for x in grid:
        current = " "
        regions = 1
        for y in x:
            if y != current:
                regions += 1
        best = max(regions,best)
    return best

print(grid_regions(grid))

from collections import defaultdict


def create_graph(matrix):
    graph = defaultdict(list)

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] == '/':
                graph[(i, j + 1)].append((i + 1, j))
                graph[(i + 1, j)].append((i, j + 1))
            elif matrix[i][j] == '%':
                graph[(i, j)].append((i + 1, j + 1))
                graph[(i + 1, j + 1)].append((i, j))

    return graph
print(create_graph(grid))
