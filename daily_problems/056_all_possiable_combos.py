
def all_combos_uniq(arr):
    # base case
    if not arr:
        return [[]]
    
    result = all_combos_uniq(arr[1:])
    return result + [subset + [arr[0]] for subset in result] 

print(all_combos_uniq([1,2,3]))
    

def steps(n):
    if n <= 1:
        return 1
    return steps(n-1) + steps(n-2)

print(steps(3))