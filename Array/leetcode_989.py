class Solution:
    def addToArrayForm(self, A, K):
        A[-1] += K
        carry = 0
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i:
                A[i - 1] += carry
        if carry:
            A = list(map(int, str(carry))) + A
        return A


    def addToArrayForm1(self, A, K):
        temp_A = 0
        res = []
        size = len(A)
        for i in range(size):
            temp_A += A[i] * 10 ** (size - i - 1)
        temp_A += K
        j = 1
        size = 1
        temp = temp_A
        while temp // 10 != 0:
            size += 1
            temp //= 10
        while j < size + 1:
            res.append(temp_A // (10 ** (size - j)))
            temp_A -= (temp_A // (10 ** (size - j))) * (10 ** (size - j))
            j += 1
        return res
s = Solution()
a = [9,9,9,9,9]
k = 1
print(s.addToArrayForm(a,k))
