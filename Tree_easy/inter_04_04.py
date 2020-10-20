# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        def height(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            L = height(node.left)
            R = height(node.right)
            if abs(L - R) > 1:
                self.flag = False
            return max(L, R) + 1
        height(root)
        return self.flag