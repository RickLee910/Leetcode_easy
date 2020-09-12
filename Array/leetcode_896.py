import operator
class Solution:
    def isMonotonic(self, A):
        i, j = 0, 0
        for n in range(len(A) - 1):
            if A[n] < A[n+1]:
                i+=1
            elif A[n] > A[n+1]:
                j+=1
            if i!=0 and j!=0:
                return False
        return i*j == 0

    def isMonotonic1(self, A):
        size = len(A)
        temp = 0  # 0:数组不升不降，1：数组上升， 2：数组下降
        if size == 1:
            return True
        for i in range(size - 1):
            if A[i] > A[i + 1]:
                temp = 2
                break
            elif A[i] < A[i + 1]:
                temp = 1
                break
            else:
                temp = 0
                continue
        if temp == 1:
            for j in range(i+1, size - 1):
                if A[j] <= A[j + 1]:
                    continue
                else:
                    return False
        elif temp == 2:
            for j in range(i + 1, size - 1):
                if A[j] >= A[j + 1]:
                    continue
                else:
                    return False
        return True

sol = Solution()
a = [1,2,3,2]
print(sol.isMonotonic(a))


