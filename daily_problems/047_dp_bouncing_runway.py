'''
bouncing airplane landing
https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/
https://www.youtube.com/watch?v=kKhnYLpME3w
'''
# plain ole recursion
def bounces(runway, planeSpeed, planePos=0):
    # in limits or problem
    if planePos < 0 or planePos >= len(runway) or runway[planePos] == 1:
        return False
    # base case
    if planeSpeed == 0:
        print(planePos)
        return True
    # try all possiable combos
    for adjustedSpeed in (planeSpeed), (planeSpeed+1), (planeSpeed-1):
        if bounces(runway, adjustedSpeed, planePos + adjustedSpeed):
            return True
    return False

print(bounces([0,0,1,0,0,0,0,0,0,0,0], 3))

# memoization

def memoBounce(runway, planeSpeed, memo, planePos):
    # check memo
    if planePos in memo and planeSpeed in memo[planePos]:
        return memo[planePos][planeSpeed] != None
    
    if planePos not in memo:
        memo[planePos] = {}
    
    # end conditions
    if planePos >= len(runway) or planePos < 0 or runway[planePos] == 1:
        return False
    
    # True end condition    
    if planeSpeed == 0:
        print(planePos)
        return True
    # recursive cases
    for adjustedSpeed in (planeSpeed-1), (planeSpeed+1), (planeSpeed):
        if memoBounce(runway, adjustedSpeed, memo, planePos+adjustedSpeed):
            memo[planePos][planeSpeed] = adjustedSpeed
            return True 
    memo[planePos][planeSpeed] = None
    return False 

print(memoBounce([0,0,1,0,0,0,0,0,0,0,0], 3, {}, 0))