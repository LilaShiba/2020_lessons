'''
This problem was asked by PagerDuty.

Given a positive integer N, find the smallest
number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with
the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.
'''

def get_divisors(n):
    '''
    get all valid divisors of n
    '''
    divisors = []
    for num in range(int(n**0.5),1,-1):
        if n%num == 0:
            divisors.append(n//num)
    return divisors

def steps(n):
    queue = [(n,0)]
    visited = set()

    while queue:
        num, moves = queue.pop(0)
        visited.add(num)

        if num == 1:
            return moves

        neighbors = get_divisors(num) + [num-1]
        for edge in neighbors:
            if edge not in visited:
                queue.append((edge, moves+1))

print(steps(100))

def steps2(n):
    # set min distance of each ith place as ith - 1 per rules
    distance = [i - 1 for i in range(n + 1)]
    # iterate over set
    for i in range(1, n + 1):
        # check all valid divisors
        for j in range(int(i ** 0.5), 1, -1):
            # if valid divisors
            if i % j == 0:
                # realx distance[i] to one of the two rules
                # 1: ith - 1
                # 2: largest divisor of a * b == n
                distance[i] = min(distance[i], distance[i // j] + 1)
        distance[i] = min(distance[i], distance[i - 1] + 1)

    return distance[-1]
print(steps2(100))

def dp_steps(n):
    # init worst case collection
    steps = [i-1 for i in range(n+1)]

    for i in range(1, n+1):
    # get steps
        for j in range(int(i**0.5),1,-1):
            if i%j == 0:
                # check all valid divisors
                steps[i] = min(steps[i], steps[i//j]+1)
        # at the end of checking all valid divisors
        # check rule 1
        steps[i] = min(steps[i], steps[i-1]+1)
    return steps[-1]

print(dp_steps(100))
