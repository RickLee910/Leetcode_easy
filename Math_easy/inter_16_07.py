class Solution:
    def maximum(self, a: int, b: int) -> int:
        temp = a - b
        k = int(temp >> 63)
        return (k + 1) * a - b * k
s = Solution()
a = 1
b = 2
print(s.maximum(a,b))