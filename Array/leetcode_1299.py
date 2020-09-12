class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        ans = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans

s =Solution()
a = [17,18,5,4,6,1]
print(s.replaceElements(a))