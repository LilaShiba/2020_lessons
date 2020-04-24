# https://algorithm-visualizer.org/dynamic-programming/knapsack-problem
def knapsack(weights, values, limit):
    # create table to hold values
    table = [0 for v in range(limit + 1)]
    # base case of grabing nada
    table[0] = 0
    # cycle through to weight limit
    for w in range(1, limit+1):
        max_weight = 0
        # cycle through all weight possiblities
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

item_weights = [0, 2, 10, 3, 6, 18]
item_values = [0, 1, 20, 3, 14, 100]
print(knapsack(item_weights, item_values, 15))

# only one of each item allowed