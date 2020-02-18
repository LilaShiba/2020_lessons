g = {1: (2,), 2: (3,), 3: (1,)} # -> True

def find_cycle(graph):
    color = {v:"white" for v in graph}
    found = [False]
    
    for vertex in graph:
        if color[vertex] == "white":
            visit(graph, vertex, color, found)
        else:
            return found

def visit(adj, v, color, found):
    if found[0] == True:
        return 
    color[v] = "gray"
    for u in adj[v]:
        if color[u] == 'gray':
            found[0] = True
            return
        if color[u] == "white":
            visit(adj, u, color, found)
    
    color[u] = "black"
            

print(find_cycle(g))    