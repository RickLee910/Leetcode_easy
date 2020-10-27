class Solution:
    def intersect(self, nums1, nums2):
        temp = {}
        ans = []
        if len(nums1) > len(nums2):
            for i,x in enumerate(nums1):
                temp[x] = temp.get(x,0) + 1
            for i in nums2:
                if i in list(temp.keys()) and temp[i] != 0:
                    temp[i] -= 1
                    ans.append(i)
        else:
            for i,x in enumerate(nums2):
                temp[x] = temp.get(x,0) + 1
            for i in nums1:
                if i in list(temp.keys()) and temp[i] != 0:
                    temp[i] -= 1
                    ans.append(i)
        return ans

s = Solution()
a = [4,9,5]
b = [9,4,9,8,4]
print(s.intersect(a,b))