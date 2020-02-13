# This problem was asked by WhatsApp.
# 
# Given an array of integers out of order, 
# determine the bounds of the smallest window
# that must be sorted in order for the entire 
# array to be sorted. For example, given 
 
arr = [3, 7, 5, 6, 9]
ans = (1, 3)
 
def order_window(arr):
    sa = sorted(arr)
    left = right = None
     
    for int in range(len(arr)):
        if sa[int] != arr[int] and left is None:
            left = int
        elif sa[int] != arr[int]:
            right = int
    return left, right

print(order_window(arr)) 