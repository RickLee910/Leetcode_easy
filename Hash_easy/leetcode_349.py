from collections import Counter
class Solution:
    def intersection(self, nums1, nums2):
        temp1 = Counter(nums1)
        temp2 = Counter(nums2)
        ans = []
        for i in temp1.keys():
            if temp2[i] >0:
                ans.append(i)
        return ans