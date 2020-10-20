import collections
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        A = list(A)
        B= list(B)
        if len(A) != len(B):
            return False
        if A == B:
            if len(set(A)) < len(A):
                return True
            return False
            '''temp_A = list(collections.Counter(A).values())
            return any(temp_A[i] > 1 for i in range(len(temp_A)))
        '''
        left = 0
        found_l = False
        right = 0
        for i in range(len(A)):
            if A[i] != B[i] and not found_l:
                left = i
                found_l = True
                continue
            if found_l and A[i] != B[i]:
                right = i
                A[right], A[left] = A[left], A[right]
                if A == B:
                    return True
                break
        return False
s =Solution()
a = "baa"
b ="baa"
print(s.buddyStrings(a,b))