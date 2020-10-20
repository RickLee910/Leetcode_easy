class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0 , len(s) - 1
        S= list(s)
        vowel = "aeiouAEIOU"
        while l < r:
            if S[l] not in vowel:
                l += 1
            if S[r] not in vowel:
                r -= 1
            if S[l] in vowel and S[r] in vowel:
                S[l],S[r] = S[r],S[l]
                l += 1
                r -= 1
        return ''.join(S)
s = Solution()
a = "leetcode"
print(s.reverseVowels(a))