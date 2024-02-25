class Solution:
    # my solution
    def find_lowest_common_ansestor(self, root, p, q):
        result = 0

        def dfs(root, p, q):
            nonlocal result
            if root == None:
                return

            if is_ancestor(root, p, q, set()):
                result = root
            dfs(root.left, p, q)
            dfs(root.right, p, q)

        def is_ancestor(root, p, q, found):
            is_root_null = root == None
            is_ancestor_possible = root.val < p.val and root.val > q.val

            if is_root_null or is_ancestor_possible:
                return False

            if root.val == p.val or root.val == q.val:
                found.add(root.val)
            if len(found) == 2:
                return True

            return is_ancestor(root.left, p, q, found) or is_ancestor(
                root.right, p, q, found
            )

        if p.val > q.val:
            p, q = q, p

        return result

    def find_lowest_ancestor_better_solution(self, root, p, q):
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
