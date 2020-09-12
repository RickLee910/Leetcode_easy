class Solution:
    def decompressRLElist(self, nums):
        ans = list()
        for i in range(0, len(nums), 2):
            ans.extend([nums[i + 1]] * nums[i])
        return ans

    def decompressRLElist1(self, nums):
        temp = []
        for i in range(len(nums) // 2):
            for j in range(nums[2*i]):
                temp.append(nums[(2*i)+1])
        return temp
sol =Solution()
a=[1,2,3,4]
a.extend([5]*3)
print(a)
