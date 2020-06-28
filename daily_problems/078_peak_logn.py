arr =[1,2,1,3,5,6,4]


def linear(arr):

    highest = 0
    idx = 0
    for x in range(1, len(arr)-1):
        if arr[x] > highest and arr[x] > arr[x+1] and arr[x] > arr[x-1]:
            highest = arr[x]
            idx = x
    return arr[x], x

print(linear(arr))

def logn(nums):
    # binary search
    lo, hi = 0, len(nums)-1

    while (lo < hi):
        mid = lo + (hi - lo) //2
        if nums[mid] < nums[mid+1]:
            lo = mid + 1
        else:
            hi = mid
    return lo 


print(logn(arr))

