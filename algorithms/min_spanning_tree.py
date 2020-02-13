
def find_min(adj_list, tree):
    best = float('inf')
    current = None
    
    for vertex in adj_list:
        for edge in adj_list[vertex]:
            if edge[0] not in tree and edge[1] < best:
                best = edge[1]
                current = edge[0]
                parent = vertex
    return current, parent

def prims(adj_list, start):
    tree = [start]
    connections = []
    
    while len(tree) < len(adj_list):
        next_vertex, parent = find_min(adj_list, tree)
        tree.append(next_vertex)
        connections.append((next_vertex, parent))
    return connections, tree


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
'f':[('g',9), ('c',2), ('b', 6), ('a',1), ('h',5)],
'h':[('f',5), ('a',6), ('e',3)],
'e':[('a',5), ('h',3)]
}


print(prims(adj_list2, 'a'))