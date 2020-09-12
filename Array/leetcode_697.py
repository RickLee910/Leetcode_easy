class Solution:
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x,0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans


sol = Solution()
a =[1,2,2,3,1]
print(sol.findShortestSubArray(a))


def findshort(nums):
    left,right,count = {}, {}, {}
    for i, x in enumerate(nums):
        if x not in left:
            left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1

    degree = max(count.values())
    ans = len(nums)
    for i in count:
        if count[i] == degree:
            res = min(ans, right[i] - left[i] + 1)

    return res

print(findshort(a))








