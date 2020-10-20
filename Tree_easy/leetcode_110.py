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
    def isBalanced(self, root) -> bool:
        def height(root) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
