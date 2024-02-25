class Solution:
    def min_cost_climbing_stairs(self, cost):
        n = len(cost)

        # we create an array where dp[i] is equal to the min cost needed to reach that step

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(1, n):
            # min cost will be min of current cost + 1 step back and current cost + 2 step back
            dp[i] = min(cost[i] + dp[i - 1], cost[i] + dp[i - 2])

        # we take min here because we can jump from n - 1 step as well without cost
        return min(dp[n - 1], dp[n - 2])


