class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        if s.isdigit() or s.isalpha():
            return ''
        temp = sorted(s)
        ans = ''
        l, r = 0, len(temp) - 1
        while l <= r:
            if l == r:
                if temp[l].isdigit():
                    ans += temp[l]
                else:
                    ans = temp[l] + ans
                break
            ans += temp[l] + temp[r]
            l += 1
            r -= 1
        return ans
s = Solution()
a = "a"
print(s.reformat(a))