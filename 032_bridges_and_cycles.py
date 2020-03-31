import unittest
# https://cp-algorithms.com/graph/bridge-searching.html
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
graph2 = {
    0:[1],
    1:[2],
    2:[3,4],
    3:[],
    4:[]
}


def find_cycles(graph):
    visited = {v:False for v in graph}
    start = list(graph.keys())[-1]
    queue = [start]
    parent = start

    while queue:
        node = queue.pop(0)

        for edge in graph[node]:
            if parent != edge:
                if visited[edge]:
                    print(edge)
                    #return True
                if not visited[edge]:
                    queue.append(edge)
        visited[node] = True
        parent = node
    return False

def find_bridges(graph):
    appeared =  {v:-1 for v in graph}
    reach = {v:-1 for v in graph}
    depth = 0
    start = list(graph.keys())[0]
    bridges =  []
    visit(graph, start, start, reach, appeared, bridges, depth)
    print(bridges)
    return bridges

def visit(graph, u,v,reach,appeared,bridges,depth):
    reach[v] = depth
    appeared[v] = depth

    for edge in graph[v]:
        if reach[edge] == -1:
            visit(graph, v, edge, reach, appeared, bridges, depth+1)
            reach[v] = min(reach[v], reach[edge])

            if reach[edge] == appeared[edge]:
                bridges.append((v,edge))

        elif edge != u:
            reach[v] = min(reach[v], appeared[edge])

def bridges(graph):
    timer = 0
    visited = {v:False for v in graph}
    dist = {v:-1 for v in graph}
    low = {v:-1 for v in graph}
    edges = []
    for vertex in graph:
        if not visited[vertex]:
            dfs_visit(graph, vertex, vertex, visited, low, dist, edges, timer)
    return edges

def dfs_visit(graph, node, parent, visited, low, dist, edges, timer):
    visited[node] = True
    low[node] = timer
    dist[node] = timer

    for edge in graph[node]:
        if edge != parent:
            if visited[edge]:
                low[node] = min(low[node], dist[edge])
            else:
                dfs_visit(graph, edge, node, visited, low, dist, edges, timer+1)
                low[node] = min(low[node], low[edge])
                if low[edge] > dist[node]:
                    edges.append((node,edge))












class CycleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_cycles(graph), True)
    def test2(self):
        self.assertEqual(find_cycles(graph2), False)
    def test3(self):
        self.assertEqual(find_bridges(graph), [(1, 5), (0, 1), (3, 4)])
if __name__ == '__main__':
    print(bridges(graph))
    print(find_bridges(graph))
    #unittest.main()
