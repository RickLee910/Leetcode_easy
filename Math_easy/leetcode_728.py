class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        ans = []
        for i in range(left, right + 1):
            temp = list(str(i))
            is_t = True
            for j in range(len(temp)):
                if i % int(temp[j]) != 0:
                    is_t = False
                    break
            if is_t:
                ans.append(i)
        return ans
s = Solution()
a = 1
b= 5
print(s.selfDividingNumbers(a,b))