class Solution:
    def numIdenticalPairs(self, nums):
        temp ={}
        count = 0
        for i, x in enumerate(nums):
            temp[x] = temp.get(x, 0) + 1
        for j in temp:
            count += (temp[j] * (temp[j] - 1)) // 2
        return count
sol = Solution()
nums = [1]
print(sol.numIdenticalPairs(nums))