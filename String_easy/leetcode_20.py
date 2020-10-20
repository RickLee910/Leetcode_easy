class Solution:
    def isValid(self, s: str) -> bool:
        temp = [0]
        for i in s:
            if i == '(' or i == '{' or i == '[':
                temp.append(i)
            elif i == ')':
                if temp[-1] == '(':
                    temp.pop()
                else:
                    return False
            elif i == '}':
                if temp[-1] == '{':
                    temp.pop()
                else:
                    return False
            elif i == ']':
                if temp[-1] == '[':
                    temp.pop()
                else:
                    return False
        if temp[-1] == 0:
            return True
        else:
            return False
s = Solution()
a = '('
print(s.isValid(a))