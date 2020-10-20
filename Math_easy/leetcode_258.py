class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            temp = list(str(num))
            temp1  = 0
            for i in temp:
                temp1 += int(i)
            num = temp1
        return num