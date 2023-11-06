class Solution:
    def is_same(self, p, q):
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val != q.val:
            return False

        return self.is_same(p.left, q.left) and self.is_same(p.right, q.right)
