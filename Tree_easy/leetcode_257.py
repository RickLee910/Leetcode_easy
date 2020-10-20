class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        if not root.left and not root.right:
            return [str(root.val)]
        ans = [str(root.val)]
        res = []

        def dfs(node):
            if not node:
                return

            ans.append("->" + str(node.val))
            dfs(node.left)
            dfs(node.right)
            if not node.left and not node.right:
                res.append("".join(ans))
            ans.pop()

        dfs(root.left)
        dfs(root.right)
        return res