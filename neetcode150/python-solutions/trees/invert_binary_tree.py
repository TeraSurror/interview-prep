class Solution:
    def invert_tree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root
