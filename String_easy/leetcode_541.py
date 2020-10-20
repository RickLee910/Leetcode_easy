class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = list(s)
        size = len(s)
        if k >= size:
            for i in range(size // 2):
                temp[i], temp[-i - 1] = temp[-i - 1], temp[i]

        else:
            for j in range(0, size, 2 * k):
                if j + k < size:
                    for i in range(k // 2):
                        temp[j + i], temp[k - i - 1 + j] = temp[k - i - 1 + j], temp[i + j]
                else:
                    for i in range((size-j) // 2):
                        temp[j + i], temp[size - i - 1] = temp[size - i - 1], temp[i + j]
        return ''.join(temp)
s = Solution()
a ="hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"

print(s.reverseStr(a,39))