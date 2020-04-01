'''
This problem was asked by Square.

A competitive runner would like to create a 
route that starts and ends at his house, with 
the condition that the route goes entirely uphill 
at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation},
 and a dictionary mapping paths between some of these locations 
 to their corresponding distances, find the length of the shortest 
 route satisfying the condition above. Assume the runner's home 
 is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.

'''
import heapq
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

# returns adj_list
# parent_node: [(distance, height, node), ....]
def make_adj_list(paths, evl):
    adj_list = {}
    for node, distance in paths.items():
        if node[0] not in adj_list:
            adj_list[node[0]] = [(distance,evl[node[1]],node[1],)]
        else:
            adj_list[node[0]].append((distance, evl[node[1]],node[1]))
            #adj_list[node[0]] = sorted(adj_list[node[0]], key=lambda x:x[2])        
    # mid = [x for x in evl.items()]
    # mid = sorted(mid, key = lambda x:x[1])
    # mid = mid[len(mid)//2]
    print(adj_list)
    return adj_list, evl[0]
def make_graph(paths):
    graph = {}
    for x,y in paths:
        if x not in graph:
            graph[x] = [y]
        else:
            graph[x].append(y)
    return graph
def topo_sort(adj_list):
    visited, stack = [], []
    for vertex in adj_list:
        if vertex not in visited:
            dfs(adj_list, vertex, visited, stack)
    return stack
    
def dfs(adj_list, vertex, visited, stack):
    visited.append(vertex)
    for v in adj_list[vertex]:
        if v not in visited:
            dfs(adj_list, v, visited, stack)
    stack.append(vertex)

def find_path(adj_list, start_height, start, end):
    
    queue = [start]
    heapq.heapify(queue)
    visited = {x:float('inf') for x in adj_list}
    #visited[0] = 0
    explored = []

    
    path = []
    while queue:
        distance, height, node = heapq.heappop(queue)
        for d,h,u in adj_list[node]:
            cost = distance + d
            if cost < visited[u] + d:
                path.append((node,u))
                visited[u] = cost      
                heapq.heappush(queue,(cost,h,u))
            if u == end:
                print('!')
                return visited,path
                
                    
    return visited, path
        

adj_list, start_height = make_adj_list(paths,elevations)
graph = make_graph(paths)
print(graph)
topo = topo_sort(graph)
print(topo)
print(find_path(adj_list, start_height,(0,0,0), 4))
