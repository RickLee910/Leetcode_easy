class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        count = 0
        temp = 0
        for i in range(len(arr1)):
            for j in arr2:
                if abs(arr1[i] - j) <= d:
                    break
                temp += 1
            if temp == len(arr2):
                count += 1
            temp = 0

        return count
