import heapq

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}

def least_cost(pipes):
    seen = set()
    distance = {} ; parent = {}
    heap = [(0,('plant', 'plant'))]
    heapq.heapify(heap)
    vertice = pipes.keys()

    while len(seen) < len(vertice):
        cost, edge = heapq.heappop(heap)
        u,v = edge
        if v not in seen:
            seen.add(v)
            if cost < distance.get(v, float('inf')):
                distance[v] = cost
                parent[v] = u

            for neighbor, cost in pipes[v].items():
                heapq.heappush(heap,(cost,(v,neighbor)))

    path = {v:[] for v in vertice}
    for u,v in parent.items():
        path[v].append(u)
    return path
print(least_cost(pipes))
