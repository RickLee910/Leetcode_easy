class Solution:
    def minCostToMoveChips(self, position):
        odd, even = 0, 0
        for i in range(len(position)):
            if position[i] % 2 == 1:
                odd += 1
            else:
                even += 1
        if odd > even:
            return even
        else:
            return odd
sol = Solution()
a = [6,4,7,8,2,10,2,7,9,7]
print(sol.minCostToMoveChips((a)))