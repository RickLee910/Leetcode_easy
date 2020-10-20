
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def preorder(self, root: 'Node'):
        if not root:
            return []
        stack, out = [root], []
        while stack:
            root = stack.pop()
            out.append(root.val)
            stack.extend(root.children[::-1])

        return out