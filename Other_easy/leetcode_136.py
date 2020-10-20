class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        i = 0
        while i + 1 <= len(nums) - 1:
            if nums[i] != nums[i+1]:
                break
            else:
                i += 2
        return nums[i]
s = Solution()
a = [4,1,2,1,2,4,3]
print(s.singleNumber(a))