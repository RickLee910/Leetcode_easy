class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        ans = TreeNode()
        cur = ans

        def inorder(node):
            if not node:
                return
            inorder(node.left)2
            nonlocal cur
            node.left = None
            cur.right = node
            cur = node

            inorder(node.right)

        inorder(root)
        return ans.right