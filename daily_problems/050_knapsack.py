# # https://algorithm-visualizer.org/dynamic-programming/knapsack-problem
def knapsack(weights, values, limit):
    # create table to hold values
    table = [0 for v in range(limit + 1)]
    # cycle through all subproblems
    for w in range(1, limit+1):
        max_weight = 0
        # cycle through all weight/value possiblities
        for v in range(1, len(weights)):
            # locate current weight and value element
            iw = weights[v]
            iv = values[v]
            # if still in the capactiy limit of problem
            if iw <= w:
                # calculate subproblem
                subproblem_value = table[w-iw] + iv
                max_weight = max(subproblem_value, max_weight)
        table[w] = max_weight
    return table

# item_weights = [0, 2, 10, 3, 6, 18]
# item_values = [0, 1, 20, 3, 14, 100]
# print(knapsack(item_weights, item_values, 15))



# def td_memo(prices, weights, limit):
#     table = [0 for x in range(limit + 1)]

#     for w in range(1, limit+1):
#         max_w = 0
#         for cut in range(1, len(weights)):
#             wi = weights[cut]
#             vi = prices[cut]
#             if wi <= w:
#                 subproblem = vi + table[w-wi]
#                 max_w = max(max_w, subproblem)
#         table[w]= max_w
#     return table

# print(td_memo(item_values, item_weights, 15))
# # only one of each item allowedr3


item_weights = [0, 2, 10, 3, 6, 18]
item_values = [0, 1, 20, 3, 14, 100]
import pprint
def one_knapsack(weights, values, limit):
    table = [[0 for x in range(limit+1)] for y in range(len(item_weights))]

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


print(one_knapsack(item_weights, item_values, 15))