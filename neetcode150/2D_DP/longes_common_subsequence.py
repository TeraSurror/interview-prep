class Solution:
    def lcs_recursive(self, text1: str, text2: str) -> int:
        def recurse(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return 1 + recurse(i - 1, j - 1)
            return max(recurse(i - 1, j), recurse(i, j - 1))

        return recurse(len(text1), len(text2))

    def lcs_dp(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]















            