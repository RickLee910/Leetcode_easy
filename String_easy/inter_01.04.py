from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        temp = Counter(s)
        count = 0
        for i in list(temp.values()):
            if i % 2 == 1:
                count += 1

            if count > 1:
                return False
        return True