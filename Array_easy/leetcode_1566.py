class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        count = 0
        if len(arr) < m * k:
            return False
        for i in range(len(arr) - m * k + 1):
            while count != k -1:
                if arr[i + m * count:i + m * (count + 1)] == arr[i + m * (count + 1):i + m * (count + 2)]:
                    count += 1
                else:
                    count = 0
                    break
        return count == k - 1
s = Solution()
a = [1,2,4,4,4,4]
print(s.containsPattern(a,1,3))