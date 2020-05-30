import random
coins = [1,2,5]
target = 11

# coin problem

def bfs_coin(coins, target):
    queue = [0]
    next_queue = []
    how_many_coins = 0
    visited = [False] * (target +1)

    while queue:
        how_many_coins += 1
        for edge in queue:
            for coin in coins:
                cc = edge + coin 
                if cc == target:
                    return how_many_coins
                if cc > target:
                    continue
                if not visited[cc]:
                    visited[cc] = True
                    next_queue.append(cc)
        queue, next_queue = next_queue, []
    return -1


def change(coins, target):
    dp = [target+1 for _ in range(target+1)]
    dp[0] = 0

    for sp in range(target+1):
        for coin in range(len(coins)):
            if coins[coin] <= sp:
                dp[sp] = min(
                    dp[sp],
                    1 + dp[sp-coins[coin]]
                )
    return dp


# paths 2

'''
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

class Node:
    def __init__(self,v):
        self.v = v
        self.r = None 
        self.l = None 
    
    def get_path(self, target):
        def find_path(root, target, current, ans):
            if root == None:
                return 
            current.append(root.v)
            if root.v == target and root.l == None and root.r == None:
                ans.append(current)
                return 

            find_path(root.l, target-root.v, current.copy(), ans)
            find_path(root.r, target-root.v, current.copy(), ans) 



        ans = []
        find_path(self, target, [], ans)
        print(ans)
        return ans
    
# partition 
def can_pp(arr):
    total = sum(arr)
    if total % 2 == 0:
        return rp(arr, 0, 0, total, {})
    return False 

def rp(arr, idx, cur_sum, total, memo):
    if (idx, cur_sum) in memo:
        return memo[(idx, cur_sum)]

    if cur_sum * 2 == total:
        return True 

    if idx >= len(arr) or cur_sum > total//2:
        return False
    
    memo[(idx, cur_sum)] = rp(arr, idx+1, cur_sum + arr[idx], total, memo) or rp(arr, idx+1, cur_sum, total, memo)
    return memo[(idx, cur_sum)]

arr = [random.randint(0,100) for x in range(15)]


# edges
graph = {
        0: [1, 2, 3],
        1: [0, 5],
        2: [0, 3],
        3: [0, 2, 4],
        4: [3],
        5: [1]
}
"""
  2 --- 0 --- 1 --- 5
   \   |
    \  |
      3 --- 4
"""
def get_edges(graph):
    visited = {x:False for x in graph}
    low = {x:float('inf') for x in graph}
    reach = low.copy()
    depth = 0
    edges = []

    for v in graph:
        if not visited[v]:
            dfs(graph,v,v,visited,low,reach,edges,depth)
    return edges 

def dfs(graph,u,v,visited,low,reach,edges,depth):
    low[v] = depth 
    reach[v] = depth 
    visited[v] = True 

    for edge in graph[v]:
        if u != edge:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs(graph, v, edge, visited, low, reach, edges, depth+1)
                low[v] = min(low[v], low[edge])
                if low[edge] > reach[v]:
                    edges.append(edge)

# merge sort
def msort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        r=l=i=0

        msort(left)
        msort(right)

        while r < len(right) and l < len(left):
            if right[r] < left[l]:
                arr[i] = right[r]
                r+=1
            else:
                arr[i] = left[l]
                l+=1
            i+= 1
        
        while r < len(right):
            arr[i] = right[r]
            r+=1
            i+=1 
        
        while l < len(left):
            arr[i] = left[l]
            l+=1
            i+=1
        return arr

# b-search

def bsearch(arr, target):
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == target:
            return arr[mid], mid 
        elif arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return False
# arr = [random.randint(0,100) for _ in range(100)]
# arr = msort(arr)
# print(bsearch(arr,18))
# rod cutting
price = [random.randint(0,50) for x in range(10)]
size = len(price)

def rod(price, size):
    dp = [0 for _ in range(size+1)]

    for cut in range(1,size+1):
        max_cut = -float('inf')
        for cost in range(cut):
            max_cut = max(max_cut, price[cost]+ dp[cut-cost-1])
        dp[cut] = max_cut
    return dp[-1]

def r(price,size, memo):
    # memoization
    if size in memo:
        return memo[size]
    # out of bounds
    if size <= 0:
        return 0
    
    max_cut = 0
    for cut in range(size):
        max_cut = max(max_cut, price[cut] + r(price, size-cut-1, memo))
    memo[size] = max_cut
    return max_cut



def rrod(price, size):
    dp = [0 for _ in range(size+1)]
    price = [0] + price 

    for cut in range(1, size+1):
        max_cut = 0
        for cost in range(1, len(price)):
            if cost <= cut:
                subproblem = price[cost] + dp[cut-cost]
                max_cut = max(subproblem, max_cut)
                dp[cut] = max_cut
    return dp

# print(rrod(price,size))
# print(r(price,size,{}))
# print(rod(price,size))

# dijkstra
import random, heapq

matrix = [[random.randint(0,10) for x in range(10)] for y in range(10)]

def dijkstra(graph, start, end, params=None):
    visited = {start:0}
    parent = {start:0}
    queue = [start]
    heapq.heapify(queue)
    row = len(graph)
    col = len(graph[0])

    while queue:
        _,weight,x,y = heapq.heappop(queue)

        # if found recreate path on graph
        if (x,y) == end:
            path = []
            current = (x,y)
            while current != (0,0):
                x,y = current
                graph[x][y] = 'X'
                current = parent[(x,y)]
            graph[0][0] = 'X'
            return weight, graph
        
        neighbors = ((x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x+1,y+1), (x-1,y+1),(x+1,y-1))
        real_neighbors = ((x,y) for (x,y) in neighbors if 0<= x < row and 0<= y < col and graph[x][y] != params)

        for cx,cy in real_neighbors:
            cost = weight + matrix[cx][cy]
            if (cx,cy) not in visited or cost < visited[(cx,cy)]:
                new_distance = abs(end[0]-cx) - abs(end[1]-cy)
                heapq.heappush(queue, (new_distance,cost,cx,cy))
                visited[(cx,cy)] = cost
                parent[(cx,cy)] = (x,y)
    return False

# bellman ford
bellman_graph = {        
            's': {'a': 0, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
}

def bellman_ford(graph,start):
    dist = {v:float('inf') for v in graph}
    dist[start] = 0

    for u in range(len(graph)-1):
        for v in graph:
            for edge, weight in graph[v].items():
                if dist[v] != float('inf') and dist[v] + weight < dist[edge]:
                    dist[edge] = dist[v] + weight

    # check neg edges
    for v in graph:
        for edge, weight in graph[v].items():
            if dist[v] != float('inf') and dist[v] + weight < dist[edge]:
                return f'neg cycle at {v} and {edge}'
    return dist
if __name__ == "__main__":
    # print(bfs_coin(coins, target))
    # print(change(coins,target))
    # print(can_pp(arr))
    print(get_edges(graph))
    # root = Node(5)
    # root.l = Node(4)
    # root.l.l = Node(11)
    # root.l.l.l = Node(7)
    # root.l.l.r = Node(2)
    # root.r = Node(8)
    # root.r.l = Node(13)
    # root.r.r = Node(4)
    # root.r.r.l = Node(5)
    # root.r.r.r = Node(1)
    # root.get_path(22)
    # arr = [random.randint(0,100) for _ in range(100)]
    # arr = msort(arr)
    # print(bsearch(arr, 18))
    # import pprint
    # pprint.pprint(matrix)
    # cost, graph = dijkstra(matrix, (0,0,0,0), (8,8))
    # print(cost)
    # pprint.pprint(graph)
    print(bellman_ford(bellman_graph, 'a'))
