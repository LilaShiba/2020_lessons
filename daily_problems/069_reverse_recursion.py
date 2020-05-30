arr = [1,2,3,4,5,6,7,8,9,10]

def r(arr,idx):
    if idx >= len(arr):
        return
    r(arr, idx+1)
    print(arr[idx])

#r(arr,0)

# def powerset(arr):
#     if not arr:
#         return [[]]
#     result = powerset(arr[1:])
#     ans = result + [x +[arr[0]] for x in result]
#     return ans



def powerset(arr):
    if not arr:
        return [[]]
    result = powerset(arr[1:])
    ans = result + [x +[arr[0]] for x in result]
    return ans

print(powerset([1,2,3]))
        
def ppset(arr):
    if not arr:
        return [[]]
    result = ppset(arr[1:])
    ans = result + [x + [arr[0]] for x in result]
    return ans

print(ppset([1,2,3,4,5]))


