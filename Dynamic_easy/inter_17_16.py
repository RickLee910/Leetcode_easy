class Solution:
    def massage(self, nums) -> int:
        if not nums:
            return 0

        mem = [0, 0]
        for n in nums:
            mem.append(max(mem[-1], mem[-2] + n))

        return max(mem)
s = Solution()
a = [2,1,4,5,3,1,1,3]
print(s.massage(a))