class Solution:
    def convertToTitle(self, n: int) -> str:
        temp1 = n // 26
        temp = n % 26

        if temp1 > 0 and temp == 0:
            temp += 26
            temp1 -= 1
        ans = [temp]
        while temp1 > 26:

            ans.append(temp1 % 26)
            temp1 = temp1 // 26
        ans.append(temp1)
        res= ''
        for i in ans[::-1]:
            if i != 0:
                res += chr(i + 64)

        return res


s = Solution()
a = 703
print(s.convertToTitle(a))