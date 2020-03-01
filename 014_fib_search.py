# This problem was asked by Netflix.
# 
# Given a sorted list of integers of length N, 
# determine if an element x is in the list without 
# performing any multiplication, division, or 
# bit-shift operations.
# 
# Do this in O(log N) time.

arr = [4, 7, 11, 16, 27, 45, 55, 65, 80, 100]
def get_fib_seq(n:int) -> list:
    a,b = 0,1
    seq = [a]
    while a < n:
        a,b = b, a+b 
        seq.append(a)
    return seq
        

def fib_search(arr:list, target:int)-> tuple:
    n = len(arr)
    fibs = get_fib_seq(n)
    offset = 0
    
    a,b = len(fibs)-2, len(fibs)-1
    
    while b > 0:
        # find the smallest Fibonacci number that is greater than or equal to the length of given array
        idx = min(offset + fibs[a], n-1)
        # if found
        if target == arr[idx]:
            return True, idx
        # if idx is larger
        elif target < arr[idx]:
            # decrease range by 2
            a-=2; b-=2
        else:
            a-=1; b-=1
            offset = idx
            print(offset,a,b)
    
    return False
    
print(fib_search(arr, 45))