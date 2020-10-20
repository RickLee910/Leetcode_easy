class Solution:
    def balancedStringSplit(self, s: str) -> int:
        temp, count = {}, 0
        for i,x in enumerate(s):
            temp[x] = temp.get(x, 0) + 1
            if len(list(temp.keys())) > 1:
                if temp['R'] == temp['L']:
                    count += 1
        return count
s = Solution()
a = 'RLRRLLRLRL'
print(s.balancedStringSplit(a))