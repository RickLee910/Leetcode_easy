class Solution:
    def findRestaurant(self, list1, list2):
        ans = {}
        res = []
        for i in range(len(list1)):
            if list1[i] in list2:
                ans[list1[i]] = i + list2.index(list1[i])
        min_index = min(ans.values())
        for i in list(ans.keys()):
            if ans[i] == min_index:
                res.append(i)
        return res