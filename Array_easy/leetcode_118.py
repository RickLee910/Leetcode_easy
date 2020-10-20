class Solution:
    def generate(self, numRows: int):
        temp = list([] for i in range(numRows))
        if numRows >= 1:
            temp[0].append(1)
        if numRows >= 2:
            temp[1].extend([1,1])
        if numRows > 2:
            temp1 = 3
            while temp1 <= numRows:
                temp[temp1-1].extend([1,1])
                for i in range(1,temp1-1):
                    temp[temp1 -1].insert(i, (temp[temp1 - 2][i - 1] + temp[temp1 - 2][i]))
                temp1 += 1
        return temp

s =Solution()
a = 10
print(s.generate(a))