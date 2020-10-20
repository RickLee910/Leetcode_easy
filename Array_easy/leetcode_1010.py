import collections
class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        temp = []
        flag = {}
        count = 0
        for i in range(60):
            temp.append(i)
        for i,x in enumerate(time):
            flag[x % 60] = flag.get(x%60,0) +1
        if 0 in flag:
            count += (flag[0] * (flag[0] - 1)) // 2
        if 30 in flag:
            count += (flag[30] * (flag[30] - 1)) // 2
        left = 1
        right = 59
        while left < right:
            if left in flag and right in flag:
                count += flag[left]* flag[right]
            left += 1
            right -= 1
        return count
s =Solution()
a =[15,63,451,213,37,209,343,319]
print(s.numPairsDivisibleBy60(a))