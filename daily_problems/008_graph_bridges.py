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

def visit(graph, u, v, reach, appeared, bridges, depth):
  reach[v] = depth
  appeared[v] = depth

  # check out neighbors
  for edge in graph[v]:
    # if not visited
    if reach[edge] == -1:
      # run dfs with vertex and edge
      # find neighbors
      visit(graph, v, edge, reach, appeared, bridges, depth + 1)
      # if it is the same, then bridge
      # the reach is min between connecting via new neighbor or old neighbor
      reach[v] = min(reach[v], reach[edge])
      
      if reach[edge] == appeared[edge]:
        bridges.append((v, edge))
      
    # if edge is not current edge
    elif edge != u:
      # reach is min between record of new neighbor or old
      reach[v] = min(reach[v], appeared[edge])

def find_bridges(graph):
  reach = {v:-1 for v in graph}
  appeared = {v:-1 for v in graph}
  depth = 0
  start = list(graph.keys())[0]
  bridges = []
  visit(graph, start, start, reach, appeared, bridges, depth)
  return bridges

print(find_bridges(graph))