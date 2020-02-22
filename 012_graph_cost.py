# This problem was asked by Twitter.

# A network consists of nodes labeled 0 to N. 
# You are given a list of edges (a, b, t), 
# describing the time t it takes for a message 
# to be sent from node a to node b. Whenever a 
# node receives a message, it immediately passes 
# the message on to a neighboring node, if possible.

# Assuming all nodes are connected, determine how 
# long it will take for every node to receive a 
# message that begins at node 0.

# For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]

# You should return 9, 
# because propagating the message 
# from 0 -> 2 -> 3 -> 4 will take that much time.
def make_adj(nodes):
  adj = dict()
  for x,y,z in nodes:
    adj[x] = adj.get(x,[]) + [(y,z)]
  return adj

def bfs(graph, start, goal):
  visited = []
  # x is the whole fucking neighbors list
  queue=[[(start,0)]]

  while queue:
    path = queue.pop(0)
    node,_ = path[-1]
    print('current node', node)
    
    if node == goal:
      cost = sum([x for node,x in path])
      return path, cost
    
    for edge,weight in graph[node]:
      print(edge)
      if edge not in visited and edge in graph:
        visited.append(edge)
        new_path = list(path)
        new_path.append((edge,weight))
        queue.append(new_path)


def prims(adj,start):
    path = [start]
    total = 0
    connections = []
    connectors = [v for v in adj]
    while len(path) < len(adj):
        next_vertex, prev_node, count = find_min(adj, path, total,connectors)
        total += count 
        path.append(next_vertex)
        connections.append((prev_node, next_vertex))
    return total, path

def find_min(adj, path, total,connectors):
    best = float('inf')
    current = None
    
    for u in path:
        for edge in adj[u]:
            if edge[0] not in path and edge[1] < best and edge[0] in connectors:
                best = edge[1]
                current = edge[0]
                prev_node = u
    return current, prev_node, best
    
        
        
        
adj = make_adj(edges)
print(adj)
print(prims(adj, 0))
#print(bfs(adj,0,3))