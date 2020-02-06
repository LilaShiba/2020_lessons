arr = [1,2,3]

def all_perms(arr):
    if len(arr) == 1:
        return [arr]
    
    ans = []
    for int in range(len(arr)):
        temp = arr[:int] + arr[int+1:]
        current = arr[int]
        for perms in all_perms(temp):
            print(perms)
            ans.append([current] + perms)
    return ans
    

def power_set(arr):
    if not arr:
        return [[]]
    
    result = power_set(arr[1:])
    ans = result + [subarr + [arr[0]] for subarr in result]
    return ans

print(power_set(arr))
print(all_perms(arr))
    