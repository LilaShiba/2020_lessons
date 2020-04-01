# This problem was asked by Pinterest.
# 
# The sequence [0, 1, ..., N] has been jumbled, and the only 
# clue you have for its order is an array representing whether 
# each number is larger or smaller than the last. Given this 
# information, reconstruct an array that is consistent with it. 
# For example, given 

arr = [None, "+", "+", "-", "+"] 
ans = [1, 2, 3, 0, 4]

def math_order(signs):
    ans = []
    hi=low=1
    for x in signs:
        if x is None:
            ans.append(hi)
        if x == "+":
            hi += 1
            ans.append(current)
        if x == "-":
            low -= 1
            ans.append(low)
    return ans

print(math_order(arr))
            
            