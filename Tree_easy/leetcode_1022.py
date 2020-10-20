class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        def dfs(root,val):
            if not root:
                return 0
            val = val << 1 or root.val
            if not root.left and not root.right:
                self.sum += val
            else:
                dfs(root.left, val)
                dfs(root.right, val)
        self.sum = 0
        dfs(root, 0)
        return self.sum
