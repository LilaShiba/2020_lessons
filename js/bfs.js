class Node{
  constructor(x,y,v){
    this.x = x;
    this.y = y;
    this.v = v;
    this.searched = false;
    this.parent = false;
  }
}

function make_array(row, col){
  let x = new Array(row);
  for (let i = 0; i < x.length; i++) {
    x[i] = new Array(col)
    for (let j = 0; j < x[i].length; j++){
      x[i][j] =
        new Node(i,j,  Math.floor(Math.random()* 10));
    }
  }
  return x
}

maze = make_array(5,5)
// console.log(maze);
console.log('start')

function bfs(maze, start, end){
  let queue = [[start]]

  while (queue.length){
    let path = queue.shift()
    let node = path[path.length-1]
    console.log('path', node)


    //if end is found
    if (node.v == end){
      console.log('found')
      return 'Found', path
      break
    }

    if (!node.searched){
      node.searched = true
      let neighbors = [[node.x+1,node.y],[node.x-1,node.y],[node.x,node.y+1],[node.x,node.y-1]]
      for(edge of neighbors){
        cx = edge[0]
        cy = edge[1]
        if ( (0 <= cx && cx < maze.length) &&( 0 <= cy && cy < maze[0].length)){
          if (maze[cx][cy].searched == false){
            u = maze[cx][cy]

            let new_path = path.map(x => x)
            console.log('new path', new_path)
            new_path.push(u)
            queue.push(new_path)

          }
        }
      }

    }
  }
return false
}

console.log( bfs(maze, maze[0][0], 5 ))
