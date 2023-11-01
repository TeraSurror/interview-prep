class Solution:
    def regex_matching(self, s, p):
        dp = dict()

        def dfs(i, j):

            if i < 0 and j < 0:
                return True
            if i < 0 and j >= 0:
                if p[j] == "*":
                    return dfs(i, j - 2)
                else:
                    return False
            if j < 0 and i >= 0:
                return False

            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == p[j] or p[j] == ".":
                dp[(i, j)] = dfs(i - 1, j - 1)
            elif p[j] == "*":
                if p[j - 1] == s[i] or p[j - 1] == ".":
                    dp[(i , j)] = dfs(i - 1, j) or dfs(i, j - 2)
                else:
                    dp[(i , j)] = dfs(i, j - 2)
            else:
                dp[(i, j)] = False

            return dp[(i , j)]
        
        return dfs(len(s) - 1, len(p) - 1)
