class Solution:
    def reorderSpaces(self, text: str) -> str:
        temp = text.split()
        count = 0
        for i in text:
            if i.isspace():
                count += 1
        if count == 0:
            return text
        if len(temp) == 1:
            return ''.join(temp) + ' ' * count

        return ((' ')*(count // (len(temp) - 1))).join(temp) + ' ' * (count % (len(temp) - 1))
s = Solution()
a = " aas"
print(s.reorderSpaces(a))