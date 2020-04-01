# MegaCorp wants to give bonuses to its employees based 
# on how many lines of codes they have written. They would 
# like to give the smallest positive amount to each worker 
# consistent with the constraint that if a developer has written 
# more lines of code than their neighbor, they should receive more money.

# Given an array representing a line of seats of employees at MegaCorp, 
# determine how much each one should get paid.

# For example, given 
arr = [10, 40, 200, 1000, 60, 30] 
# you should return 
ans = [1, 2, 3, 4, 2, 1]

def bonus_pay(arr):
    n = len(arr)
    bonus = [None]*n
    
    if arr[0] > arr[1]:
        pay = 2
    else:
        pay = 1

    bonus[0] = pay 
    
    for person in range(1, len(arr)-1):
        if arr[person] > arr[person-1]:
            pay += 1
            bonus[person] = pay
        else:
            pay = 1
            if arr[person] > arr[person+1]:
                pay +=1
                bonus[person] = pay 
            else:
                bonus[person] = pay
    
    if arr[-1] > arr[-2]:
        bonus[-1] = pay + 1
    else:
        bonus[-1] = pay - 1
    return bonus

def bp(arr):
    arr.insert(0, float('-inf'))
    arr.append(float('inf'))
    n = len(arr)
    bonus = [None]*n
    pay = 0
    
    for p in range(1, n-1):
        if arr[p] > arr[p-1]:
            pay += 1
            bonus[p] = pay 
            flag = True
        elif arr[p] < arr[p-1] and arr[p] > arr[p+1]:
            pay = 2
            bonus[p] = pay
        else:
            pay = 1
            bonus[p] = pay
            
    return bonus[1:-1]
        
            
print(bonus_pay(arr))
print(bp(arr))