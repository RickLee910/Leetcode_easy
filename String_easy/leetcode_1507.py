class Solution:
    def reformatDate(self, date: str) -> str:
        Months = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        ans = ''
        ans += date[-4:] + '-'
        ans += Months[date[-8:-5]] + '-'
        temp = ''
        for i in date[0:2]:
            if i.isdigit():
                temp += i
            else:
                temp = '0' + temp
        return ans + temp
s = Solution()
a = "2th Sep 2052"
print(s.reformatDate(a))