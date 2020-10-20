class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        aver = sum(A) // 3
        Sum = 0
        count = 0

        for i in range(len(A)):
            Sum += A[i]
            if Sum == aver:
                count += 1
                Sum = 0
        if count < 3:
            return False
        else:
            return True
s = Solution()
a = [10,-10,10,-10,10,-10,10,-10]
print(s.canThreePartsEqualSum(a))