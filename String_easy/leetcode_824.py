class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        words = S.split()
        end = 'a'
        for i in range(len(words)):

            word = words[i]
            if word[0] in s:
                words[i] = words[i] + "ma" + end
            else:
                words[i] = word[1:] + word[0] + "ma" + end
            end += "a"

        return " ".join(words)
s = Solution()
a = "I speak Goat Latin"
print(s.toGoatLatin(a))