class Solution:
    def reverse(self, x: int) -> int:
        temp = list(str(abs(x)))
        ans = int("".join(temp[::-1])) if x > 0 else -int("".join(temp[::-1]))
        if -2 ** 31 <= ans <= 2 ** 31 - 1:
            return ans
        else:
            return 0
