class Solution:
    def shuffle(self, nums, n):
        size = len(nums)
        for i in range(n,size):
            temp = nums[i]
            nums.pop(i)
            nums.insert(2*(i-n) +1, temp)

        return nums
s = Solution()
a =[1,2,3,4,4,3,2,1]
print(s.shuffle(a,4))