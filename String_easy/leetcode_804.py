class Solution:
    #hash
    def uniqueMorseRepresentations(self, words) -> int:
        Morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---",".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        dic = {}

    #双循环
    def uniqueMorseRepresentations1(self, words) -> int:
        Morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        temp = []
        for i in words:
            word = ''
            for j in i:
                word += Morse[ord(j) - 97]
            if word not in temp:
                temp.append(word)
        return len(temp)
s = Solution()
a = ["gin", "zen", "gig", "msg"]
print(s.uniqueMorseRepresentations(a))
