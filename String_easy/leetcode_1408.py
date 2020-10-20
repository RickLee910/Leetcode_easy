class Solution:
    def stringMatching(self, words):
        ans = []

        for i in words:
            count = 0
            temp = words.copy()
            temp.remove(i)
            for j in temp:
                if i in j:
                    count += 1
                if count == 1:
                    ans.append(i)
                    break
        return ans
s = Solution()
a= ["mass","as","hero","superhero"]
print(s.stringMatching(a))