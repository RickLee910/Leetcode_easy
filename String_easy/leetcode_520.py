class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word[0].isupper():
            return any([word[1:].islower()]) or any([word[1:].isupper()])
        for i in word:
            if i.isupper():
                return False
        return True
s =Solution()
a = "FLaG"
print(s.detectCapitalUse(a))
