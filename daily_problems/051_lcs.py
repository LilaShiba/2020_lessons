arr = [50, 3, 10, 7, 40, 80]
arr2 = [3, 10, 2, 1, 20,0]
import random 
arr3 = [random.randint(0,10) for x in range(5)]
print(arr3)

def bottom_up(arr):
    table = [1 for x in range(len(arr))]

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                table[i] = max(table[i], table[j] + 1)
    return table


def lcs(arr, best_count):
    n = len(arr)

    if n == 1:
        return 1
    
    
    count = 1
    for x in range(idx+1):
        if arr[x] < arr[x+1]:
            count += 1
    best_count = max(best_count, count)
    return best_count

#print(lcs(arr3, 0))
print(bottom_up(arr3))