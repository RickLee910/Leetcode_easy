class Solution:
    def search(self, nums, target: int) -> int:
        temp = {}
        for i,x in enumerate(nums):
            temp[x] = temp.get(x,0) + 1
        if target not in temp.keys():
            return 0
        return temp[target]