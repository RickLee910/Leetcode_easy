class Solution:
    def smallerNumbersThanCurrent1(self, nums):
        n = len(nums)
        cnt, vec = [0] * 101, [0] * n
        for num in nums:
            cnt[num] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        for i in range(n):
            if nums[i]:
                vec[i] = cnt[nums[i] - 1]
        return vec


    def smallerNumbersThanCurrent(self, nums):
        temp = []
        size = len(nums)
        for i in range(size):
            count = 0
            for j in range(size):
                if nums[j] < nums[i]:
                    count += 1
            temp.append(count)
        return temp
sol =Solution()
a = [7,7,7,7]
print(sol.smallerNumbersThanCurrent1(a))
