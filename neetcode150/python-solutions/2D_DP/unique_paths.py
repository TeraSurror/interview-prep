class Solution:
    def unique_paths(self, m, n):
        dp = [[1] * len(n)] * len(m)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]