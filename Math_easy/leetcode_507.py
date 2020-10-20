class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0: return False
        i = 1
        s = 0
        while i <= sqrt(num):
            if num % i == 0:
                s += i
                if i*i != num:
                    s += (num / i)
            i += 1
        if (s - num) == num: return True
        else: return False