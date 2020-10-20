from collections import Counter
import re
class Solution:
    def checkRecord(self, s: str) -> bool:
        temp = Counter(s)
        count = 0
        if temp['A'] <= 1:
            for i in s:
                if i == "L":
                    count += 1
                    if count >2:
                        return False
                else:
                    count = 0
            return True
        else:
            return False