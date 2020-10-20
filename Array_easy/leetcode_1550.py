class Solution:
    def threeConsecutiveOdds(self, arr):
        res = 0
        for i in arr:
            if i % 2 == 1:
                res += 1
            else:
                res = 0
            if res == 3:
                return True
        return False
s = Solution()
a = [1,2,34,3,4,5,7,23,12]
print(s.threeConsecutiveOdds(a))