class Solution:
    def find_max_depth(self, root):
        def dfs(root, curr_depth):
            if root == None:
                return curr_depth

            return max(dfs(root.left, curr_depth + 1), dfs(root.right, curr_depth + 1))

        return dfs(root, 0)
