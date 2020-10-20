class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        temp1, temp2 = [],[]
        def dfs(node, l):
            if node:
                if not node.left and not node.right:
                    l.append(node.val)
                dfs(node.left,l)
                dfs(node.right,l)
        dfs(root1,temp1)
        dfs(root2,temp2)
        return True if temp1 == temp2 else FalseeNode) -> bool: