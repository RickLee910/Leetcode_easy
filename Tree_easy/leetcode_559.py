
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif root.children == []:
            return 1
        else:
            h = [self.maxDepth(c) for c in root.children]
            return max(h) + 1