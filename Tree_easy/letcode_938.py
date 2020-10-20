class Solution:
    #1
    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        self.Sum = 0
        def DFS(node):
            if not node:
                return 0
            if node.val > R:
                DFS(node.left)
            elif node.val < L:
                DFS(node.right)
            else:
                self.Sum += node.val
                DFS(node.left)
                DFS(node.right)
        DFS(root)
        return self.Sum
    #2
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        temp = []
        def dfs(node):
            if node:
                temp.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        temp.sort()

        ans = 0
        for i in range(len(temp)):
            if temp[i] >= L and temp[i] <= R:
                ans += temp[i]
        return ans