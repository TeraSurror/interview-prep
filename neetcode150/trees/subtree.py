class Solution:
    def isSubtree(root, subRoot):
        def is_same_tree(p, q):
            if p == None and q == None:
                return True

            if p and q and p.val == q.val:
                return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
            else:
                return False

        def dfs(root, subRoot):
            if subRoot == None:
                return True
            if root == None:
                return False
            if root and subRoot and root.val == subRoot.val:
                if is_same_tree(root, subRoot):
                    return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)
