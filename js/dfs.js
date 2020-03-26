let dfs = (node, adj_list, cache) =>{
  if (!cache.includes(node)){
    cache.push(node)
    for (edge of adj_list[node]){
      dfs(edge, adj_list, cache)
    }
  }
  return cache
}

graph = {0: [1, 2, 3], 1: [3], 2: [4], 3: [4, 0], 4: [0]}
console.log(dfs(0,graph,[]))
