

item_weights = [0, 2, 10, 3, 6, 18]
item_values = [0, 1, 20, 3, 14, 100]
import pprint
def one_knapsack(weights, values, limit):
    table = [[0 for x in range(limit+1)] for y in range(len(weights))]

    # cycle all options
    for i in range(1, len(weights)):
        # cycle all places from 1 ... limit
        for w in range(1, limit+1):
            # grab current weight/value
            iw = item_weights[i]
            iv = item_values[i]
            # if we can add shit
            if iw <= w:
                table[i][w] = max(table[i-1][w-iw]+iv, table[i-1][w])
            else:
                table[i][w] = table[i-1][w]




def knapsack(weights, values, limit):
    # col should be every option for every sp
    # row should be for every sp (sp = at this weight what is the max amount)
    table = [[0 for _ in range(limit+1)] for _ in range(len(weights))]

    # for every sp
    for w in range(1, len(weights)):
        # within every iteration of the sp's weight limit
        for l in range(1, limit+1):
            # set current weight and value to sp value
            iw = weights[w]
            iv = values[w]
            # stay in weight bounds
            if iw <= l:
                # compare and take best
                table[w][l] = max(table[w-1][l-iw] + iv, table[w-1][l])
            else:
                # default on prev value as that's the best for the current sp
                table[w][l] = table[w-1][l]
    return table[-1][-1]

    


def meow(price, weight, target):
    dp = [[0 for _ in range(target+1)]for _ in range(len(weight))]

    for sp in range(1, len(weight)):
        for cut in range(1, target+1):
            cw = weight[sp]
            cv = price[sp]
            # if I fits
            if cw <= cut:
                dp[sp][cut] = max(dp[sp-1][cut-cw] + cv, dp[sp-1][cut])
            else:
                dp[sp][cut] = dp[sp-1][cut]
    return dp[-1][-1]


#print(one_knapsack(item_weights, item_values, 10))
#pprint.pprint(knapsack(item_weights, item_values, 10))
import random
price = [random.randint(0,100) for _ in range(100)]
weight = [random.randint(0,100) for _ in range(100)]
import time
start_time = time.time()

print(knapsack(price, weight, 100))
print(meow(weight, price, 100))

print("--- %s seconds ---" % (time.time() - start_time))

