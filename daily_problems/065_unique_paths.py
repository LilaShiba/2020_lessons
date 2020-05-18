# https://www.youtube.com/watch?v=6qMFjFC9YSc
# https://leetcode.com/problems/unique-paths/

import pprint

def unique_paths(col,row):
    # create table
    table = [[None for x in range(col)] for y in range(row)]
    # set row 0 to all 1's
    table[0] = [1 for x in range(col)]
    # set all col 0's to 1's
    for x in range(row):
        table[x][0] = 1
    # compute subproblems
    # 
    for i in range(1, row):
        for j in range(1,col):
            # # add how many ways there are to get cell we are on
            # # cell above us and to our left
            above = table[i-1][j]
            left = table[i][j-1]
            table[i][j] = above + left
    return table[-1][-1]


def unique_paths2(row,col):
    # create table
    matrix = [[1 for _ in range(col)]for _ in range(row)]

    for x in range(1,row):
        for y in range(1, col):
            matrix[x][y] = matrix[x-1][y] + matrix[x][y-1]

    return matrix 

pprint.pprint(unique_paths2(3,2))
pprint.pprint(unique_paths(3,2))