class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        low, high = 0, len(nums)
        def build(nums,low,high):
            if high <= low:
                return
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            node.left = build(nums,low,mid)
            node.right = build(nums,mid+1, high)
            return node
        return build(nums, low, high)