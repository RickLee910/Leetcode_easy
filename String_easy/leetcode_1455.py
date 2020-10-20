class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        temp = sentence.split()
        l = len(searchWord)
        for i in temp:
            if i[:l] and i[:l] == searchWord:
                return temp.index(i) + 1
        return -1
s = Solution()
a = "this problem is an easy problem"
b = "pasdro"
print(s.isPrefixOfWord(a,b))