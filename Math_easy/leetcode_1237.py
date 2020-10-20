class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1,z+1):
            left, right = 1, z
            while left < right:
                mid = (left + right) // 2
                res = customfunction.f(x,mid)
                if res < z:
                    left = mid + 1
                else:
                    right = mid
            if customfunction.f(x,left) == z:
                ans.append([x,left])
        return ans
