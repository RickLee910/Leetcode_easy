class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in s:
            if (ord(i) > 64 and ord(i) < 91) or (ord(i) > 96 and ord(i) < 123)or (ord(i) > 47 and ord(i) < 58):
                temp.append(i)
        for i in range(len(temp) // 2):
            if temp[i].lower() != temp[-i - 1].lower():
                return False
        return True
s = Solution()
a = "A man, a plan, a canal: Panama"
print(s.isPalindrome(a))