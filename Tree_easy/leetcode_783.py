class Solution:

    '''
    def minDiffInBST(self, root: TreeNode) -> int:
        temp = []
        def dfs(node):
            if not node:
                return
            temp.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        temp.sort()

        mindif, dif = abs(temp[0] - temp[1]), 0
        for i in range(len(temp) - 1):
            dif = abs(temp[i] - temp[i + 1])
            mindif = min(dif, mindif)
        return mindif
    '''