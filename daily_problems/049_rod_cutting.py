import random
price = [random.randint(0,50) for x in range(10)]
size = len(price)

def top_rod(price, size, memo):
    # check memo
    if size in memo:
        return memo[size]
    # base case 
    if size <= 0:
        return 0
    # recursion 
    max_value = -float('inf')
    for cut in range(0, size):
        max_value = max(max_value, price[cut] + top_rod(price, size-cut-1, memo))
    memo[size] = max_value
    return max_value

print(top_rod(price, size, {}))

def bottom_up_rod(price, size):
    table = [0 for x in range(size + 1)]

    for all_cuts in range(1, size+1):
        max_value = -float('inf')
        for cut in range(all_cuts):
            max_value = max(max_value, price[cut] + table[all_cuts-cut-1])
        table[all_cuts] = max_value

    print(table) 
    return table[-1]

print(bottom_up_rod(price,size))