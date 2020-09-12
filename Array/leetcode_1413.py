class Solution:
    def minStartValue(self, nums) -> int:
        min_res = 0
        temp = 0
        for i in nums:
            temp = i+temp
            min_res = min(temp, min_res)
        if min_res <= 0:
            min_res = 1 - min_res
        return min_res
s = Solution()
a = [1,-2,-3]
print(s.minStartValue(a))