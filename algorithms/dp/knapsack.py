

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

    pprint.pprint(table)



def knapsack(weights, values, limit):
    table = [[0 for _ in range(limit+1)] for _ in range(len(weights))]

    
    for w in range(1, len(weights)):
        for l in range(1, limit+1):
            iw = weights[w]
            iv = values[w]
            if iw <= l:
                table[w][l] = max(table[w-1][l-iw] + iv, table[w-1][l])
            else:
                table[w][l] = table[w-1][l]
    return table

               


print(one_knapsack(item_weights, item_values, 15))
print(knapsack(item_weights, item_values, 15))