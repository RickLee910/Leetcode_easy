def titleToNumber(self, s: str) -> int:
    # 初始化结果 ans = 0，遍历时将每个字母与 A 做减法，因为 A 表示 1，所以减法后需要每个数加 1，计算其代表的数值 num = 字母 - ‘A’ + 1. 因为有 26 个字母，所以相当于 26 进制，每 26 个数则向前进一位. 所以每遍历一位则ans = ans * 26 + num. 以 ZY 为例，Z 的值为 26，Y 的值为 25，则结果为 26 * 26 + 25=701.
    ans = 0
    for i in range(len(s)):
        num = ord(s[i]) - ord('A') + 1
        ans = ans * 26 + num
    return ans