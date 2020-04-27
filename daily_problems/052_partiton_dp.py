'''
Partition problem is to determine whether a given 
set can be partitioned into two subsets such that 
the sum of elements in both subsets is same.
'''

def navie(arr, n):
    current_sum = sum(arr)
    if current_sum % 2 != 0:
        return False 
    
    return navie_recursion(arr,n,current_sum//2)
    
def navie_recursion(arr,n,current_sum):
    if current_sum == 0:
        return True 
    
    if n == 0 and current_sum != 0:
        return False
    
    if arr[n-1] > current_sum:
        return navie_recursion(arr,n-1,current_sum)
    
    return navie_recursion(arr,n-1,current_sum) or navie_recursion(arr,n-1, current_sum - arr[n-1])


def recursion_partition(arr, n):
    current_sum = sum(arr)
    if current_sum % 2 == 0:
        return recursion(arr, n, current_sum//2)
    return False

def recursion(arr, n, current_sum):
    if current_sum == 0:
        return True 
    if n == 0 and current_sum != 0:
        return False
    if arr[n-1] > current_sum:
        return recursion(arr, n-1, current_sum)
    
    ''' else, check if sum can be obtained by any of  
    the following 
    (a) including the last element 
    (b) excluding the last element'''

    return recursion(arr, n-1, current_sum) or recursion(arr, n-1, current_sum - arr[n-1])

import random
arr = [random.randint(0,100) for x in range(15)]
print(arr)
print(navie(arr,len(arr)))
print(recursion_partition(arr, len(arr)))
