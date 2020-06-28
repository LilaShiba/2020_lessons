class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        def cycle(node):
            # if seen twice, cycle
            if node in exploring:
                return True
            # if already explored, chill out
            elif node in explored:
                return False
            # We are actively exploring connects to this node
            exploring.add(node)
            # continue to search all connections to this node
            for edge in graph[node]:
                # dfs
                if cycle(edge):
                    return True
            exploring.remove(node)
            explored.add(node)
            return False
        
        # keep track of nodes during state
        exploring, explored = set(), set()
        
        # create graph  
        graph = collections.defaultdict(list)
        for p, c in prerequisites:
            graph[p].append(c)
            
        # iterate through all vertices that connect to others
        for clss in list(graph):
            if clss not in explored:
                if cycle(clss): 
                    return False
        return True