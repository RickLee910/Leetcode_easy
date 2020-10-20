class Solution:
    def readBinaryWatch(self, num: int):
        return [f"{h}:{m:2d}" for h in range(12) for m in range(60) if (bin(h)+bin(m)).count('1') == num]

s = Solution()
a = 3
print(s.readBinaryWatch(a))