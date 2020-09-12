class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        dif = max(candies) - extraCandies
        res = []
        for i in candies:
            if i >= dif:
                res.append(True)
            else:
                res.append((False))
        return res