'''
This problem was asked by Google.

In linear algebra, a Toeplitz matrix is one in which the elements
on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.

'''

matrix = [
    [1, 2, 3,4, 8],
    [5, 1, 2, 3, 4],
    [4, 5, 1, 2, 3],
    [7, 4, 5, 1, 2]
]

def toeplitz(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for row in range(n):
        if not same(matrix, row, 0):
            return False

    for col in range(m):
        if not same(matrix, 0, col):
            return False
    return True


def same(matrix, row, col):
    n, m = len(matrix), len(matrix[0])
    start = matrix[row][col]
    while row < n and col < m:
        if matrix[row][col] != start:
            return False
        row += 1
        col += 1

    return True

def tp(matrix):
    values = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i-j) not in values:
                values[(i-j)] = matrix[i][j]
            elif values[(i-j)] != matrix[i][j]:
                return False
    return True
print(tp(matrix))
print(toeplitz(matrix))
