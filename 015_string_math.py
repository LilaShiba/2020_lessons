# This problem was asked by Facebook.
# 
# Given a string consisting of parentheses, 
# single digits, and positive and negative 
# signs, convert the string into a mathematical 
# expression to obtain the answer.
# 
# Don't use eval or a similar built-in parser.

# For example, given 
maths = '-1 + (2 + 3)'
# polish = -1 2 3 + +
# you should return 
ans = 4


'''
    +
   / \
  +    -
 / \  / \
2  3     1

'''
class Node:
    def __init__(self, v, left=None, right=None):
        self.v = v
        self.left = left 
        self.right = right
        
        
def math_str(exp):
    expresions = ["+", "-", "/", "*", "(", ")"]
    exp = exp.replace(" ", "")

    return list(''.join(exp))

def solve_tree(root):
    if root.v == "+":
        return solve_tree(root.left) + solve_tree(root.right)
    elif root.v == "-":
        return solve_tree(root.left) - solve_tree(root.right)
    elif root.v == "*":
        return solve_tree(root.left) * solve_tree(root.right)
    elif root.v == "/":
        return solve_tree(root.left) // solve_tree(root.right)
    else:
        return root.v
        
def solve_polish(seq: list) -> int:
    stack = []
    ops = ['*', '+', "-", "/", "^"]
    for char in seq:
        if char in ops:
            expression1, expression2 = stack.pop(), stack.pop()
            if char == '*':
                stack.append(expression1*expression2)
            elif char == "/":
                stack.append(expression1/expression2)
            elif char == "+":
                stack.append(expression1+expression2)
            elif char == "^":
                stack.append(expression1**expression2)
            else:
                stack.append(expression1-expression2)
        else:
            stack.append(char)
    return stack.pop()
            
        
print(math_str(maths))
print(solve_polish([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))
    