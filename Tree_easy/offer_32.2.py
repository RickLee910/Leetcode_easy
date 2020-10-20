
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        temp = []

        def search(node):
            if node:
                search(node.right)
                temp.append(node.val)
                search(node.left)

        search(root)
        temp.sort()
        return temp[-k]


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.count = 1

        def search(node):
            if node:
                search(node.right)
                if self.count == k:
                    self.res = node
                self.count += 1
                search(node.left)

        self.res = TreeNode()
        search(root)

        return self.res.val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root: return
        if k <= 0: return
        self.count = 0
        self.k = k
        self.ret = ""
        self.travel(root)
        return self.ret

    def travel(self, root):
        if not root: return
        self.travel(root.right)
        self.count += 1
        if self.count == self.k:
            self.ret = root.val
        elif self.count > self.k:
            return
        else:
            self.travel(root.left)t[int]]: