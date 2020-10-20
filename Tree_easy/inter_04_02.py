# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(nums, low, high):
            if high <= low:
                return
            mid = (high + low) // 2
            node = TreeNode(nums[mid])
            node.left = build(nums, low, mid)
            node.right = build(nums, mid + 1, high)
            return node

        return build(nums, 0, len(nums))
