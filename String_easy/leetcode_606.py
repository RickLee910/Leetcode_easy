# Definition for a binary tree node.

'''
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        if not t.left and not t.right:
            return str(t.val)

        if not t.right:
            return str(t.val) +"("+self.tree2str(t.left)+")"

        return str(t.val)+"("+self.tree2str(t.left)+")"+"("+self.tree2str(t.right)+")"
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def list_to_binarytree(self,nums):
        def level(index):
            if index >= len(nums) or nums[index] is None:
                return None

            root = TreeNode(nums[index])
            root.left = level(2 * index + 1)
            root.right = level(2 * index + 2)
            return root

        return level(0)

    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        if not t.left and not t.right:
            return str(t.val)

        if not t.right:
            return str(t.val) +"("+self.tree2str(t.left)+")"

        return str(t.val)+"("+self.tree2str(t.left)+")"+"("+self.tree2str(t.right)+")"

s =Solution()
a = s.list_to_binarytree([1,2,3,4])
print(s.tree2str(a))


