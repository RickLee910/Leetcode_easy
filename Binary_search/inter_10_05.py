class Solution:
    def findString(self, words, s: str) -> int:
        return words.index(s) if s in words else -1