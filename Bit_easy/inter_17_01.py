class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b != 0:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)

s = Solution()
a = 12
b = 5
print(s.add(a,b))