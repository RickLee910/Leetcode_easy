class Solution:
    def minCostClimbingStairs(self, cost):
        a1, a2 = 0,0
        size = len(cost)
        for i in range(-1,-size - 1, -1):
            a1, a2 = cost[i] + min(a1,a2), a1
        return min(a1,a2)
s = Solution()
a = [10,15,20,10]
print(s.minCostClimbingStairs(a))
