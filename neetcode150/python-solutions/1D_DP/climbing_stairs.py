class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        a = 1
        b = 2
        result = a + b
        for _ in range(3, n):
            a = b
            b = result
            result = a + b
        
        return result
        