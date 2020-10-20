class Solution:
    def findTilt(self, root: TreeNode) -> int:
        temp = 0
        def gradient(node):
            nonlocal temp
            if not node:
                return 0
            l = gradient(node.left)
            r = gradient(node.right)
            temp += abs(l - r)
            return l + r + node.val
        gradient(root)
        return temp