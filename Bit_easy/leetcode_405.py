
class Solution:
    def toHex(self, num: int) -> str:
        hex_str = '0123456789abcdef'
        num &= 0xffffffff  # 高位都是 0，移位也是补 0
        digits = []
        # 手动执行一次循环
        lowbit4 = num & 0xf
        num >>= 4
        digits.append(hex_str[lowbit4])
        # 开始执行 while 循环
        while num:
            lowbit4 = num & 0xf
            num >>= 4
            digits.append(hex_str[lowbit4])

        # 最后反转一下再连接
        return ''.join(reversed(digits))

s = Solution()
a =-1
print(s.toHex(a))