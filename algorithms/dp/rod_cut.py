arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
ans = 22
import random
arr2 = [random.randint(0,50) for x in range(50)]
size = len(arr2)
def bottom_up(price, size):
    table = [0 for x in range(size+1)]

    for i in range(1, size+1):
        max_cut = -float('inf')
        for j in range(i):
            max_cut = max(max_cut, price[j] + table[i-j-1])
        table[i] = max_cut
    print(table)
    return table[size]
print(bottom_up(arr2, size))


def top_down(prices,size, memo):
    if size in memo:
        return memo[size]
    if size <= 0:
        return 0
    max_value = -float('inf')
    for i in range(0, size):
        max_value = max(max_value, prices[i] + top_down(prices, size-i-1, memo))
    memo[size] = max_value
    return max_value

print(top_down(arr2,size, {}))
