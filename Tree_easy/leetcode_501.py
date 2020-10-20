class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        if not root.left and not root.right: return [root.val]
        temp = {}

        def dfs(node):
            if not node:
                return

            if node.val not in temp:
                temp[node.val] = 1
            else:
                temp[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        ans = []
        for i in list(temp.keys()):
            if temp[i] == max(temp.values()):
                ans.append(i)
        return ans
