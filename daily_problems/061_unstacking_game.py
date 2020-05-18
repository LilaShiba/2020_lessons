# https://www.youtube.com/watch?time_continue=733&v=NuGDkmwEObM @ 1:05

def stacky(stack):
    unstack = [stack]
    ans = 0

    while unstack:
        to_sum = unstack.pop(0)
        ans += to_sum - 1
        if to_sum -1 > 0:
            unstack.append(to_sum-1)
    return ans

#print(stacky(8))

def factorial(stack,memo):
    if stack == 1 or stack == 0:
        return stack

    if stack in memo:
        return memo[stack]
    
    ans = stack * factorial(stack-1, memo)
    memo[stack] = ans 
    return ans
  
     
def r_unstack(stack):
    if stack == 2:
        return 1
    return r_unstack(stack-1) + stack-1


#print(r_unstack(5))
print(factorial(5,{}))

