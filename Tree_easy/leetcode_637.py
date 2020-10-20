class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        temp = []
        q = collections.deque([root])
        while q:
            n = len(q)
            S = 0
            for _ in range(n):
                node = q.popleft()
                S += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            temp.append(S / n)
        return temp