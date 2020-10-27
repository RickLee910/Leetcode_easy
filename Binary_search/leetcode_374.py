
class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1,n

        while l < r:
            mid = (l + r) // 2
            temp = guess(mid)
            if temp == 0:
                return mid
            elif temp == 1:
                l = mid + 1
            elif temp == -1:
                r = mid
        return l