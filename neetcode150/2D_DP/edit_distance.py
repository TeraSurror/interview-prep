class Solution:
    def edit_distance(self, word1, word2):
        dp = dict()

        def dfs(i, j):

            if j == len(word2):
                return len(word2) - i
            if i == len(word1):
                return len(word2) - j

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] != word2[j]:
                dp[(i, j)] = min(
                    1 + dfs(i + 1, j + 1), 
                    1 + dfs(i + 1, j),
                    1 + dfs(i, j + 1)
                )
            else:
                dp[(i, j)] = dfs(i + 1, j + 1)

            return dp[(i, j)]
        
        return dfs(0, 0)
