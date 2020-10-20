class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1)-m):
            nums1.pop()
        for j in range(len(nums2)-n):
            nums2.pop()
        nums1.extend(nums2)
        nums1.sort()
    def merge1(self, nums1, m, nums2, n):
        temp = {}
        temp1 = []
        for i,x in enumerate(nums1):
            if m == 0:
                break
            temp[x] = temp.get(x, 0) + 1
            if i == m - 1:
                break
        for j, x in enumerate(nums2):
            if n == 0:
                break
            temp[x] = temp.get(x, 0) + 1
            if j == n - 1:
                break
        nums1.clear()
        temp1 = list(temp.keys())
        temp1.sort()
        for j in temp1:
            nums1.extend([j] * temp[j])

nums1 = [3,0,0]
m = 1
nums2 = [2,5,6,0,0]
n = 3
s = Solution()
s.merge(nums1,m,nums2,n)
print(nums1)