class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(node):
            if not node:
                return 0
            l_d = depth(node.left)
            r_d = depth(node.right)
            return max(l_d, r_d) + 1
        return depth(root)
