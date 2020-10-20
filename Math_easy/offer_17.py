class Solution:
    def printNumbers(self, n: int) -> List[int]:
        ans = []
        for i in range(1,10 ** n):
            ans.append(i)
        return ans