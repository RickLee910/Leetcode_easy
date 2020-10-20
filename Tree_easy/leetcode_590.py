class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(root,ans):
            if root == None:
                return
            for i in root.children:
                dfs(i,ans)
            ans.append(root.val)
            return ans
        dfs(root, ans)
        return ans
