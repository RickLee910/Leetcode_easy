class Solution:
    def findLHS(self, nums: List[int]) -> int:
        temp = {}
        for i,x in enumerate(nums):
            temp[x] = temp.get(x, 0) + 1
        key = sorted(list(temp.keys()))
        max_l = 0
        for i in range(len(key) - 1):
            if key[i] + 1 == key[i+1]:
                max_l =max(max_l, temp[key[i]] + temp[key[i+1]])
        return max_l