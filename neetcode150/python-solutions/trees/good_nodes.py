class Solution:
    def goodNodes(self, root):
        count = 0

        def dfs(root, greatest_yet):
            nonlocal count
            if root == None:
                return
            if root.val >= greatest_yet:
                count += 1
            greatest_yet = max(greatest_yet, root.val)
            dfs(root.left, greatest_yet)
            dfs(root.right, greatest_yet)

        dfs(root, root.val)
        return count
