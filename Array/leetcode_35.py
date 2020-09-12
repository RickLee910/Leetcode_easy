class Solution:
    #二分法
    def searchInsert1(self, nums, target):
        first, end = 0, len(nums)
        while first < end:
            mid = (first + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            else:
                end = mid
        return first

    #利用list特性，巧妙计算
    def searchInsert(self, nums, target):
        for i in nums:
            if i >= target:
                return nums.index(i)
        return len(nums)



a = [1,3,5,6]
sol = Solution()
print(sol.searchInsert(a, 4))
