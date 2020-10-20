class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        temp = ['0']+ list(str(int(a) + int(b)))
        for i in range(len(temp) - 1, 0, -1):
            if int(temp[i]) <= 1:
                ans = temp[i] + ans
            else:
                ans = str(int(temp[i]) % 2) + ans
                temp[i - 1] = str(int(temp[i - 1]) + 1)
        if temp[0] == '1':
            ans = temp[0] + ans
        return ans
s = Solution()
a = '0'
b ='1'
print(s.addBinary(a,b))