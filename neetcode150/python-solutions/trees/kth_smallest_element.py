class Solution:
    def kth_smallest_element(self, root, k):
        node_list = []

        def inorder(root):
            nonlocal node_list
            if len(node_list) == k:
                return node_list[len(node_list) - 1]

            if root == None:
                return

            inorder(root.left)
            node_list.append(root.val)
            inorder(root.right)

        inorder(root)
        return node_list[k - 1]
