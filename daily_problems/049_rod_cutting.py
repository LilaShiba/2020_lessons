import random
price = [random.randint(0,50) for x in range(10)]
size = len(price)


def r_rod(price, size, memo):
    if size in memo:
        return memo[size]
    
    if size <= 0:
        return 0
    
    max_cut = -float('inf')
    for cut in range(0,size):
        max_cut = max(max_cut, price[cut] + r_rod(price, size-cut-1, memo))
    
    memo[size] = max_cut
    return max_cut

def r_table(price,size):
    table = [0 for x in range(size+1)]

    for cut in range(1, size+1):
        max_cut = 0 
        for current_size in range(cut):
            max_cut = max(max_cut, price[current_size] + table[cut-current_size-1])
        table[cut] = max_cut
    return table

    
print('r_table', r_table(price,size))
print('r_rod', r_rod(price, size, {}))



def rod(price,size):
    table = [0 for x in range(size+1)]
    for current_cut in range(1, size+1):
        max_value = 0
        for current_value in range(current_cut):
            this_cut =  price[current_value] + table[current_cut - current_value-1]
            max_value = max(this_cut, max_value)
        table[current_cut] = max_value
    return table


print('rod', rod(price, size))


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

print('top rod', top_rod(price, size, {}))

def bottom_up_rod(price, size):
    table = [0 for x in range(size + 1)]

    for all_cuts in range(1, size+1):
        max_value = -float('inf')
        for cut in range(all_cuts):
            max_value = max(max_value, price[cut] + table[all_cuts-cut-1])
        table[all_cuts] = max_value
    return table[-1]

print('bottom up', bottom_up_rod(price,size))


def roddy(arr,target):
    table = [0 for x in range(target+1)]

    for cut in range(1, target+1):
        max_value = -float('inf')
        for limit in range(cut):
            max_value = max(max_value, arr[limit] + table[cut-limit-1])
        table[cut] = max_value
    return table

print(roddy(price, size))
