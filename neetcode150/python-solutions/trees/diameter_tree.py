class Solution:
    def find_diameter(self, root):
        result = 0

        def dfs(root):
            nonlocal result

            if root == None:
                return 0

            max_left = dfs(root.left)
            max_right = dfs(root.right)
            max_node = max_left + max_right
            result = max(result, max_node)

            return 1 + max(max_left, max_right)

        dfs(root)
        return result
