class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        temp = set()
        max_num, min_num = arr[0],arr[0]
        for num in arr:
            temp.add(num)
            max_num = max(num, max_num)
            min_num = min(num,min_num)
        n = len(temp)
        if (max_num - min_num) / (n -1) == 0:
            return True
        return False
    def canMakeArithmeticProgression1(self, arr) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] !=diff:
                return False
        return True
s = Solution()
a= [3,5,1]
print(s.canMakeArithmeticProgression(a))