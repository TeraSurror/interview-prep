class Solution:
    def min_cost_climbing_stairs(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(1, n):
            dp[i] = min(cost[i] + dp[i - 1], cost[i] + dp[i - 2])

        return dp[ - 1]


