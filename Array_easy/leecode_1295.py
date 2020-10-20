class Solution:
    def findNumbers(self, nums) -> int:
        res = 0
        for i in nums:
            if (i // 10 >0 and i // 10 < 10) or (i // 1000 >0 and i // 1000 < 10)or (i // 100000 >0 and i // 100000 < 10):
                res += 1
        return res
