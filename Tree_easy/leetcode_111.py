class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        minDep,Dep = 209000, 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    minDep = min(minDep, Dep)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            Dep += 1    
        return minDep