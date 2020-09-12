class Solution:
    def majorityElement(self, nums):
        size = len(nums)
        step = size >> 1
        nums.sort()
        for i in range(size - step):
            if nums[i] == nums[i + step]:
                return nums[i]
        return -1
    def majorityElement1(self, nums):
        temp = {}
        size = len(nums)
        for i,x in enumerate(nums):
            temp[x] = temp.get(x, 0) + 1
        max_count = max(temp.values())
        if max_count > size // 2:
            return list(temp.keys())[list(temp.values()).index(max_count)]
        else:
            return -1
sol = Solution()
a = [1]
print(sol.majorityElement(a))