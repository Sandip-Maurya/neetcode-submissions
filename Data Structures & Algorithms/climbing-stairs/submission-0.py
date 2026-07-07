class Solution:
    def climbStairs(self, n: int, memo: dict = {}) -> int:
        if n == 1 or n == 2:
            return n
        if n in memo:
            return memo[n]
        return self.climbStairs(n-1) + self.climbStairs(n-2)