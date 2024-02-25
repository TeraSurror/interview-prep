class Solution:
    def max_sum_path(self, root):
        res = root.val

        def dfs(root):
            nonlocal res
            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, root.val + max(left, 0) + max(right, 0))
            return root.val + max(max(left, 0), max(right, 0))

        dfs(root)
        return res
