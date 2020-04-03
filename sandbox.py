# # graph = {
# #     0: [1, 2, 3],
# #     1: [0, 5],
# #     2: [0, 3],
# #     3: [0, 2, 4],
# #     4: [3],
# #     5: [1]
# # }
# #
# # """
# # 2 --- 0 --- 1 --- 5
# #   \   |
# #    \  |
# #       3 --- 4
# # """
# #
# # def find_edges(graph):
# #     reach = {v:-1 for v in graph}
# #     low = {v:-1 for v in graph}
# #     visited = {v:False for v in graph}
# #     depth = 0
# #     edges = []
# #
# #     for vertex in graph:
# #         if not visited[vertex]:
# #             dfs(graph, vertex, vertex, reach, low, visited, depth, edges)
# #         return edges
# #
# # def dfs(graph, u, v, reach, low, visited, depth, edges):
# #     reach[v] = depth
# #     low[v] = depth
# #     visited[v] = True
# #
# #     for edge in graph[v]:
# #         if edge != u:
# #             if visited[edge]:
# #                 low[v] = min(low[v], reach[edge])
# #             else:
# #                 dfs(graph, v, edge, reach, low, visited, depth+1, edges)
# #                 low[v] = min(low[v], low[edge])
# #                 if low[edge] > reach[v]:
# #                     edges.append(edge)
# #
# # edges = find_edges(graph)
# # print("Edges:",edges)
# # cycle = graph.keys() - edges
# # print("Cycles:",cycle)
#
#
import random
s = [random.randint(0,1) for x in range(10)]
# print(s)
#s1 = [0,1,1,0,1,0,0,1,0]
#s2 = [1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
#s = [0, 1, 1, 0, 0, 1, 0, 1, 0, 1]



def move(seats):
    # calculate indices of taken seats
    people = [i for i, x in enumerate(seats) if x == 1]
    n = len(people)
    # find median of seats taken
    median = people[n//2]
    cost = 0
    seats[median] = "x"

    current_seat = median
    current_person = n//2 -1

    # seats[current_seat] = 'c'

    left_people = people[:n//2]
    print(left_people)
    # need to swap?
    mark = False
    need_to_loop = False
    for x in seats[:median]:
        if x == 1:
            mark = True
        if x == 0 and mark:
            need_to_loop = True
            break
    # if need to swap, move to right
    if need_to_loop:
        while len(left_people) > 0:
            if seats[current_seat] == 0:
                current_person = left_people.pop(-1)
                while current_person >= current_seat and left_people:
                    current_person = left_people.pop(-1)
                print(current_person)

                seats[current_seat], seats[current_person] = seats[current_person], seats[current_seat]
                #seats[people[current_person]] = '0'

            current_seat -= 1










    return seats

print(move(s))
