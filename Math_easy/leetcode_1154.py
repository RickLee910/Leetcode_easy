class Solution:
    def dayOfYear(self, date: str) -> int:
        month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        ans = 0
        if int(date[:4]) % 4 == 0 and int(date[:4]) % 100 != 0 or int(date[:4]) % 400 == 0:
            month[2] += 1
        for i in range(1,int(date[5:7])):
            ans += month[i]
        return ans + int(date[8:])
s = Solution()
a = "1900-03-25"
print(s.dayOfYear(a))