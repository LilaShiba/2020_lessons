import random 
arr = [random.randint(0,100) for x in range(100)]
arr = sorted(arr)
print(arr)

def b_search_i(arr, target):
    lo, hi = 0, len(arr)-1
    

    while lo <= hi:
        mid = (lo + hi)//2
        if arr[mid] < target:
            lo = mid + 1
        elif arr[mid] > target:
            hi = mid -1 
        elif target == arr[mid]:
            return mid, arr[mid]
    
    return False

print(b_search_i(arr, 10))

def b_search_r(arr, target, l, r):
    
    if r >= l:
        
        
        mid = (l+r)//2
        
        if target == arr[mid]:
            return mid, target
        
        if arr[mid] > target:
            r = mid - 1
            return b_search_r(arr, target, l, r)
        else:
            l = mid + 1
            return b_search_r(arr, target, l, r)
    
    return -1
            
    

print(b_search_r(arr, 10, 0, len(arr)-1))        
        
        
    