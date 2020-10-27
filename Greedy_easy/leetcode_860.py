class Solution:
    def lemonadeChange(self, bills) -> bool:
        temp = {5:0,10:0,20:0}
        for i in bills:
            if i== 10:
                if temp[5] > 0:temp[5] -= 1
                else:return False
            elif i == 20:
                if temp[10] > 0 and temp[5] > 0:
                    temp[5] -= 1
                    temp[10] -= 1
                elif temp[5] > 2:
                    temp[5] -= 3
                else:return False
            temp[i] += 1
        return True
