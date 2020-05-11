'''
This problem was asked by Airbnb.

You are given a huge list of airline ticket prices between 
different cities around the world on a given day. These are 
all direct flights. Each element in the list has the format 

(source_city, destination, price).

Consider a user who is willing to take up to k connections from  
origin city A to their destination B. Find the cheapest fare possible 
for this journey and print the itinerary for that journey.

For example, our traveler wants to go from JFK to LAX 
with up to 3 connections, and our input flights are as follows:

[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
Due to some improbably low flight prices, 
the cheapest itinerary would be 
JFK -> ATL -> ORD -> LAX, costing $440.

'''

flights = [
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
    ('HKG', 'ORD', 250)
]

def make_adj(flights):
    adj_list = {}
    for x,y,z in flights:
        if  x not in adj_list:
            adj_list[x] = [(y,z)]
        else:
            adj_list[x].append((y,z))
    return adj_list

# gives shortes path
def bfs(flights, start, stop, layovers):
    queue = [[(start,0)]]
    visited = []
    price = 0

    while queue:
        path = queue.pop(0)
        node, cost = path[-1]

        if node == stop:
            return path, cost

        if node not in visited:
            visited.append(node)
        
        for edge, new_cost in flights[node]:
            if edge not in visited and edge in flights:
                new_path = list(path)
                new_path.append((edge, cost+new_cost))
                queue.append(new_path)
    return False

import heapq
def dijkstra(flights, start, stop, layovers):
    queue = [(0, start, 0)]
    heapq.heapify(queue)
    parent = {start:0}
    visited = {start:0}

    while queue:
        current_cost, node, hops = heapq.heappop(queue)

        if node == stop:
            return parent, visited, current_cost, hops
        
        for edge, cost in flights[node]:
            new_cost = cost + current_cost
            if edge not in parent or new_cost < visited[edge] and hops <= layovers:
                heapq.heappush(queue, (new_cost, edge, hops+1))
                visited[edge] = new_cost
                parent[edge] = node 
    return False, False, False, False

def recreate_path(start, stop, parent):
    path = []
    current_node = stop
    while current_node != start:
        path.append(current_node)
        current_node = parent[current_node]
    
    path.append(start)
    return path[::-1]


def dijkstra(flights, start, stop, layovers):
    queue = [(0,start,0)]
    heapq.heapify(queue)
    visited = {}
    parent = {start:0}

    while queue:
        cost, node, count = heapq.heappop(queue)

        if node == stop:
            path = recreate_path(start, stop, parent)
            print(f'The cost of the trip is {cost}. There are {count} layovers. The flight path is {path}')
            return True

        for edge, next_cost in flights[node]:
            new_cost = next_cost + cost
            if (edge not in parent or new_cost < visited[edge]) and (count+1 <= layovers):
                parent[edge] = node 
                visited[edge] = new_cost
                heapq.heappush(queue, (new_cost, edge, count+1))
    return False
        




if __name__ == "__main__":
    flights = make_adj(flights)
    start = 'JFK'
    stop = 'ORD'
    # dijkstra + path recreation
    print(dijkstra(flights, start, stop, 2))
    
