'''
A group of houses is connected to the main water plant by means of a set of pipes.
A house can either be connected by a set of pipes extending directly to the plant,
 or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where A, B, and C are houses, and
arrows represent pipes:

A <--> B <--> C <--> plant
Each pipe has an associated cost, which the utility company would like to minimize.
 Given an undirected graph of pipe connections, return the lowest cost configuration
 of pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A,
plant to B, and B to C, for a total cost of 16.

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}


'''
import heapq

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}

def dikstras(adj_list):
    heap = [(0,('plant','plant'))]
    heapq.heapify(heap)
    seen = set()
    costs = {} ; prev = {}
    vertices = adj_list.keys()

    while len(seen) < len(vertices):
        cost, edge = heapq.heappop(heap)
        u,v = edge

        if v not in seen:
            if cost < costs.get(v, float('inf')):
                costs[v] = v
                prev[v] = u

            for neighbor, cost in adj_list[v].items():
                heapq.heappush(heap, (cost, (v, neighbor)))
            seen.add(v)

    path = {v:[] for v in vertices}
    for u,v in prev.items():
        path[v].append(u)
    return path

print(dikstras(pipes))
