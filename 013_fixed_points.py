# This problem was asked by Apple.
# 
# A fixed point in an array is an element
#  whose value is equal to its index. 
#  Given a sorted array of distinct elements, 
#  return a fixed point, if one exists. Otherwise, 
#  return False.

# For example, given 
arr = [-6, 0, 2, 40] 
# you should return 2. 
# Given 
arrf = [1, 2, 7, 8, 9] 
# you should return False

# On
def find_fixed(arr):
    points = []
    for idx, num in enumerate(arr):
        if num == idx:
            points.append(num)
    if len(points) == 0:
        return False
    return points

# Log N (for sorted)    
def b_search(arr):
    
    low, hi = 0, len(arr)
    
    while low <= hi:
        mid = (low+hi)//2
        
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            hi = mid - 1
    return False
    

    
print(find_fixed(arrf))
print(b_search(arrf))