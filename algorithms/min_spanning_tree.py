
def find_min(adj_list, tree):
    best = float('inf')
    current = None
    
    for vertex in tree:
        for edge in adj_list[vertex]:
            if edge[0] not in tree and edge[1] < best:
                best = edge[1]
                current = edge[0]
                parent = vertex
    return current, parent, best

def prims(adj_list, start):
    tree = [start]
    connections = []
    total = 0
    while len(tree) < len(adj_list):
        next_vertex, parent, best = find_min(adj_list, tree)
        tree.append(next_vertex)
        total += best
        connections.append((parent, next_vertex))
    return connections, tree, total


adj_list = {
'a':[('b', 8), ('c', 6), ('d', 5)],
'b':[('a', 8), ('d', 4)],
'c':[('a',6), ('d', 3)],
'd':[('a',5), ('b',4), ('c',3)]
}

adj_list2 = {
'a':[('b',8), ('f',1), ('h', 6), ('e',5)],
'b':[('a',8), ('c',4), ('f',2)],
'c':[('b',4), ('f',2), ('g',7)],
'g':[('c',7), ('f',9)],
'f':[('g',9), ('c',2), ('b', 6), ('a',1), ('h',5), ('e',1)],
'h':[('f',5), ('a',6), ('e',3)],
'e':[('a',5), ('h',3), ('f',1)]
}


print(prims(adj_list2, 'a'))