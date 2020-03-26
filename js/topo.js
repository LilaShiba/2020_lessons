let make_matrix = (row, col) => {
    let matrix = Array(row)
    for (let x = 0; x <= row; x++){
      matrix[x] = new Array(col)
      for (let y = 0; y <= col; y++){
        matrix[x][y] = Math.floor(Math.random()*10)
      }
    }
  return matrix
}

console.log(make_matrix(5,5))
graph = {0: [1, 2, 3], 1: [3], 2: [4], 3: [4, 0], 4: [0]}


let topo = (node, adj_list, cache,stack) =>{
  if (!cache.includes(node)){
    cache.push(node)

    for (edge of adj_list[node]){
      topo(edge, adj_list, cache,stack)
    }
    stack.push(node)
  }
  return stack
}

graph = {0: [1, 2, 3], 1: [3], 2: [4], 3: [4, 0], 4: [0]}
console.log(topo(0,graph,[],[]))
