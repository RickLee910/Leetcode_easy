import collections
class Solution:
    def numSmallerByFrequency(self, queries, words):
        fword = [word.count(min(word)) for word in words]
        fquery = [query.count(min(query)) for query in queries]
        ans = [sum(i > q for i in fword) for q in fquery]
        return ans


s = Solution()
a = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
b =["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
print(s.numSmallerByFrequency(a,b))

