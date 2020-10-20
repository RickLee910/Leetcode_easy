import collections
class Solution:
    def countCharacters(self, words, chars):
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans

    def countCharacters1(self, words, chars):
        size = len(words)
        long = 0
        temp = 0
        temp1 = {}
        a = 'qwertyuiopasdfghjklzxcvbnm'
        for i,x in enumerate(a):
            temp1[x] = temp1.get(x,0)
        for i in chars:
            if i in temp1:
                temp1[i] += 1
        temp2 = temp1.copy()
        for i in range(size):
            if len(words[i]) > len(chars):
                continue
            else:
                for j in range(len(words[i])):
                    if temp1[words[i][j]] > 0 and temp2[words[i][j]] > 0:
                        temp += 1
                        temp2[words[i][j]] -= 1
                    else:
                        break
                if temp == len(words[i]):
                    long += temp
                temp = 0
                temp2 = temp1.copy()
        return long
s = Solution()
a = ["hello","world","leetcode"]
b = "welldonehoneyr"
print(s.countCharacters(a,b))