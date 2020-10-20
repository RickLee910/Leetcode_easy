import collections
import random
class Solution:
    #投票算法，假设一个众数c，每有一个c,count++,少一个count--
    def majorityElement2(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
    #随机法，随机选出一个值，若满足要求则输出，否则继续
    def majorityElement4(self, nums):
        major_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for num in nums if num == candidate) > major_count:
                return candidate
    #利用字典翻转记录次数，并根据value返回key值
    def majorityElement(self, nums):
        count = {}
        size = len(nums)
        for i, x in enumerate(nums):
            count[x] = count.get(x, 0) + 1
        res = max(count.values())
        key = list(count.keys())[list(count.values()).index(res)]
        if res > size / 2:
            return key
        else:
            return 0
    def majorityElement1(self, nums):
        a = collections.Counter(nums)
        return a.most_common(1)[0][0]
sol = Solution()
a = [3,2,3,1,2,3,3]
print(sol.majorityElement4(a))
