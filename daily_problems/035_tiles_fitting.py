'''
This problem was asked by Wayfair.

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.

'''
def ways_tiles(n):
    d = [0] * (n+1)
    t = [0] * (n+1)

    d[1] = 1; d[2] = 2
    t[1] = 1; t[2] = 2

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2] + 2 * t[i-2]
        t[i] = t[i-1] + d[i - 1]
    return d[n]

print(ways_tiles(4))


def w_tiles(n):
    a,b = 1,2
    for x in range(2, n):
        a,b = a+b, a
    return a

print(w_tiles(4))
