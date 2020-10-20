class Solution:
    def exchangeBits(self, num: int) -> int:
        return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)


s = Solution()
a = 1
print(s.exchangeBits(a))