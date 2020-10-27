class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        temp = {}
        for i,x in enumerate(arr):
            temp[x] = temp.get(x,0) + 1
        if len(list(temp.keys())) != len(set(list(temp.values()))):
            return False
        else:
            return True