class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        ans, temp  = '', '11'
        for i in range(2,n + 1):
            count = 1
            ans = ''
            for j in range(len(temp) - 1):
                if temp[j] == temp[j + 1]:
                    count += 1
                else:
                    ans += str(count) + temp[j]
                    count = 1
                if j == len(temp) - 2:
                    ans += str(count) + temp[ j + 1]
            temp = ans
        return ans
s = Solution()
for i in range(8):
    print(s.countAndSay(i))