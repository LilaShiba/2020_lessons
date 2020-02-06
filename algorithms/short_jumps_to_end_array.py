arr = [2,0,5,8,1,1,1,1,4,2]

def shortest_jumps(arr):
    jumps = 1
    stairs = arr[0]
    ladder = arr[0]
    n = len(arr)
    
    for x in range(1, n):
        # end case
        if n - 1 == x:
            return jumps
        # tells us what index we can reach  
        ladder = max(x + arr[x], ladder)
        stairs -= 1

        if stairs == 0:
            jumps += 1
            if x >= ladder:
                return -1
                
            stairs = ladder - x
        
print(shortest_jumps(arr))        
        