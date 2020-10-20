class Solution:
    def countSegments(self, s: str) -> int:
        S = list(s)
        count = 0
        for i in range(len(S)):
            if (i == 0 or S[i - 1] == ' ') and S[i] != ' ':
                count += 1
        return count

s = Solution()
a = "#@#!%^&*()_+QWERTYUIawefaef"
print(s.countSegments(a))

