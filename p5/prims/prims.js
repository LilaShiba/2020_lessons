let vertices = [];
let new_paths = [];

function setup(){
    createCanvas(400,400)
}

function mousePressed(){
    let v = createVector(floor(mouseX), floor(mouseY));
    vertices.push(v)
}

function draw(){
    background(220);
    if (new_paths.length > 1){
        let prev_node = new_paths[0]
        fill(255,0,0)
        ellipse(prev_node.x, prev_node.y, 8,8)
        for(let i= 1; i < new_paths.length; i++){
            fill(255);
            stroke(255);
            ellipse(vertices[i].x, vertices[i].y, 8,8)
            fill(255,0,0)
            line(vertices[i].x, vertices[i].y, prev_node.x, prev_node.y)
            prev_node = new_paths[i]    
        }
    }   
    if (vertices.length > 1 && new_paths.length < 1){
        let prev_node = vertices[0]
        fill(255,0,0)
        ellipse(prev_node.x, prev_node.y, 8,8)
        for(let i= 1; i < vertices.length; i++){
            fill(255);
            stroke(255);
            ellipse(vertices[i].x, vertices[i].y, 8,8)
            line(vertices[i].x, vertices[i].y, prev_node.x, prev_node.y)
            prev_node = vertices[i]    
        }
    }
}

function paths(){
    console.log('starting prims')
    let copy_vertices = [...vertices]
    let adj_list = get_adj(vertices)
    while (copy_vertices.length > 0){
        node = copy_vertices.pop()
        let new_line  = get_manhattan(node)
        new_node = createVector(new_line[0], new_line[1])
        new_paths.push(new_node)
    }
    console.log(`${new_paths}`)
}

function get_adj(){
    let ans = {}
    for (let i = 0; i < vertices; i++){
        ans[vertices.i] = i
    }
    console.log('ADJ LIST: ' + ans)
    return ans
}

function get_manhattan(node){
    let best_dist = 10000
    let best_node = (0,0)
    // edit here
    for (edge of vertices){
        let this_dist = abs(node.x - edge.x) + abs(node.x - edge.x)
        if (best_dist > this_dist){
            best_node = [node.x, node.y]
            best_dist = this_dist
        }
    }
    console.log("best node "+ best_node)
    return best_node
}


document.getElementById('prims').onmouseover = paths;
