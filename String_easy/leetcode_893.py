class Solution:
    def numSpecialEquivGroups(self, A) -> int:
        return len({(''.join(sorted(str[::2]) +sorted(str[1::2]))) for str in A})
