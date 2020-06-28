# https://leetcode.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        return self.getSquare(n, {})
    
    
    def getSquare(self, n, memo):
        
        if n < 4:
            return n
        
        if n in memo:
            return memo[n]
        
        count = n
        
        for i in range(1, n):
            if i*i <= n:
                count = min(count, self.getSquare(n-(i*i), memo) + 1)
            else:
                break
        memo[n] = count
        return count