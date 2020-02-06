adj_list = {
0: [1],
1: [2],
2: [3,1],
3: [4],
4: [5],
5: [0]
}


def is_safe(adj_list, colors, ans):
    last_color = ans[-1]
    last_vertex = len(ans)-1
    neighbors = [x for x in adj_list[last_vertex] if x < last_vertex]
    
    for edge in neighbors:
        if ans[edge] == last_color:
            return False
    return True
    

def backtrack(adj_list, colors, ans=[]):
    if len(adj_list) == len(ans):
        return True, ans
    for color in range(colors):
        ans.append(color)
        if is_safe(adj_list, color, ans):
            if backtrack(adj_list, colors, ans):
                return True, ans
        ans.pop(0)
    return False
    

print(backtrack(adj_list, 2))