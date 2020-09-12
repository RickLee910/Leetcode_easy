import time
class Solution:
    def missingNumber(self, nums):
        for i in range(0, len(nums)):
            if nums[i] != i:
                return nums[i] - 1
        return len(nums)



#用时最少答案
'''
class Solution:
    def missingNumber(self, nums):
        a = len(nums)
        for i in range(a):
            if i != nums[i]:
                if i == 0 and nums[0] == 1:
                    return 0
                else:
                    return i
        return i+1

'''

sol = Solution()
a = [0]
start = time.time()
b = sol.missingNumber(a)
end = time.time()
print(b, end - start)
print(5 // 2)