def dfs(node, adj_list, cache, target):
    if node not in cache:
        cache.append(node)
        if node == target:
            return True
        for edge in adj_list[node]:
            dfs(edge, adj_list, cache)
    return cache