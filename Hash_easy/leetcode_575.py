from collections import Counter
class Solution:
    def distributeCandies(self, candies) -> int:
        temp = Counter(candies)
        l = len(candies)// 2
        return min(l, len(temp.keys()))
