import collections
class Solution:
    def findPairs(self, nums, k: int) -> int:
        temp = collections.Counter(nums)
        temp_key = list(temp.keys())
        count = 0
        if k == 0:
            for i in temp_key:
                if temp[i] > 1:
                    count += 1
            return count
        if k < 0:
            return count
        for i in temp_key:
            if i + k in temp_key:
                count += 1
        return count
s = Solution()
a = [3,1,4,1,5]
print(s.findPairs(a, -1))
