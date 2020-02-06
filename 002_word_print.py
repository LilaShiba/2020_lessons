# This problem was asked by PayPal.
# 
# Given a string and a number of lines k, print the string in zigzag form. 
# In zigzag, characters are printed out diagonally from top left to bottom 
# right until reaching the kth line, then back up to top right, and so on.
# 
# For example, given the sentence "thisisazigzag" and k = 4, you should print:
# 
# t     a     g
#  h   s z   a
#   i i   i z
#    s     g

import pprint

word = 'thisisazigzag'
k = 4

def zig_zag(word, k):
    n = len(word)
    matrix = [[" " for col in range(n)] for row in range(k)]
    pprint.pprint(matrix)
    row = 0
    
    for col, letter in enumerate(word):
        matrix[row][col] = letter
        
        # set direction
        if row == 0:
            desc = True
        elif row == k-1:
            desc = False
        # set next row
        if desc:
            row += 1
        else:
            row -= 1
    
    for line in matrix:
        print("".join(line))
    
            
    
    #return ans

zig_zag(word,k)
        
            