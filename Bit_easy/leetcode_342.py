import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return math.log2(num) % 2 == 0