import collections
class Solution:
    def findLucky(self, arr) -> int:
        temp_arr = sorted(arr, reverse=True)
        temp = collections.Counter(temp_arr)
        for i in list(temp.keys()):
            if i == temp[i]:
                return i
        return -1