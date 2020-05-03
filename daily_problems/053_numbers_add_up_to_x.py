'''
This problem was asked by Microsoft.

Given an array of numbers and a number k, 
determine if there are three entries in the 
array which add up to the specified number k. 
For example, given [20, 303, 3, 4, 25] and k = 49,  
return true as 20 + 4 + 25 = 49
'''
import pprint
# return true or false
# return items
def add_me(arr, target):
    table = [[0 for _ in range(target+1)] for _ in range(len(arr))]
    keep = []
    for num in range(len(arr)):
        for current_limit in range(1, target+1):
            iw = arr[num]
            if iw <= current_limit and table[num-1][current_limit-iw] + iw > table[num-1][current_limit]:
                table[num][current_limit] = table[num-1][current_limit-iw] + iw
                if iw not in keep:
                    keep.append(iw)
            else:
                table[num][current_limit] = table[num-1][current_limit]
    
    # for i in range(len(arr), 0, -1):
    #     if table[]
    # print(table)
    return get_items(keep, target)
    
def get_items(keep, target):
    keep = sorted(keep, key = lambda x:x, reverse=True)
    ans = []
    for x in keep:
        target -= x
        ans.append(x)
        if target  == 0:
            break
    return ans




import pprint
arr = [20, 303, 3, 4, 25]
m = (add_me(arr, 49))
print(m)

# for 2 entires 

def two_entries(arr, target):
    for x in range(len(arr)//2):
        if target - arr[x] in arr:
            return target-arr[x], arr[x]
    return False 

print(two_entries(arr, 45))
            
