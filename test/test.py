# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.rank = 0
        self.res = 0

        def inorder(node):
            if not node: return
            inorder(node.right)
            self.rank += 1
            if self.rank == k:
                res = node.val
                return
            inorder(node.left)

        inorder(root)
        return self.res

s = Solution1()
t = TreeNode(1)
s.kthLargest(t, 0)