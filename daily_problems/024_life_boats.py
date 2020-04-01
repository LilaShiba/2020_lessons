'''
This problem was asked by Glassdoor

An imminent hurricane threatens the coastal town of 
Codeville. If at most two people can fit in a rescue 
boat, and the maximum weight limit for a given boat 
is k, determine how many boats will be needed to save everyone.

For example, given a population with weights 
[100, 200, 150, 80] and a boat limit of 200, 
the smallest number of boats required will be three.

'''

people = [100, 200, 150, 80]
limit = 200
ans = 3

def boats_needed(arr):
    arr = sorted(arr, key=lambda x:x, reverse=True)
    lo = len(arr)-1
    boat = 0
    n = len(arr)-1
    
    while hi < len(arr)-1:
        
        if arr[hi] + arr[lo] <= 200:
            arr.pop(lo)
        
        boat += 1
        hi += 1 
        lo = len(arr)-1
        

    return boat
print(boats_needed(people))
    