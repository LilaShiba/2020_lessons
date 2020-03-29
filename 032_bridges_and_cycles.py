import unittest
graph = {
    0: [1, 2, 3],
    1: [0, 5],
    2: [0, 3],
    3: [0, 2, 4],
    4: [3],
    5: [1]
}

graph2 = {
    0:[1],
    1:[2],
    2:[3,4],
    3:[],
    4:[]
}


def find_cycles(graph):
    stack = [list(graph.keys())[0]]
    visited = {v:False for v in graph}

    while stack:
        node = stack.pop(0)
        if not visited[node]:
            visited[node] = True
            for edge in graph[node]:
                if visited[edge]:
                    print(edge)
                    return True
                else:
                    stack.append(edge)
    return False


class CycleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_cycles(graph), True)
    def test2(self):
        self.assertEqual(find_cycles(graph2), False)

if __name__ == '__main__':
    unittest.main()
