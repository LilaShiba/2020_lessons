'''
This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct,
find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its
left and right neighbors. It is guaranteed that the first and
last elements are lower than all others.
'''

import random
arr = [random.randint(0,100) for x in range(10)]
arr[0] = -1
arr[-1] = -3

def peak(array):
    n = len(array)
    start, end = 0, n - 1

    while start + 1 <= end:
        mid = start + (end - start) // 2

        if array[mid - 1] < array[mid] > array[mid + 1]:
            return array[mid]
        elif array[mid] < array[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    return array[start]

print(peak(arr))

def peak_unsorted(arr):
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid] < arr[mid+1]:
            lo = mid + 1
        else:
            hi = mid - 1
    return arr[lo]

print(arr)
print(peak_unsorted(arr))
