class Solution:
    def validate_bst(self, root):
        def dfs(root, left, right):
            if root == None:
                return True

            if root.val <= left or root.val >= right:
                return False

            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)

        return dfs(root, float("-inf"), float("inf"))
