class Solution:
    def heightChecker(self, heights) -> int:
        temp = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if temp[i] != heights[i]:
                count += 1
        return count
s =Solution()
a = [1,1,4,2,1,3]
print(s.heightChecker(a))