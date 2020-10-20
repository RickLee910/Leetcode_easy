class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        temp = []
        for i in range(len(S) + 1):
            temp.append(i)
        left, right = 0, len(S)
        ans = []
        for i in S:
            if i == 'I':
                ans.append(temp[left])
                left += 1
            else:
                ans.append(temp[right])
                right -= 1
        ans.append(temp[left])
        return ans