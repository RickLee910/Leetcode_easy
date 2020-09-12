class Solution:
    def masterMind(self, solution, guess):
        temp = {}
        res = []
        a,b = 0, 0
        for i,x in enumerate(solution):
            temp[x] = temp.get(x,0) + 1
        for i, y in enumerate(guess):
            res.append(guess[i])
        for i in range(4):
            if guess[i] == solution[i]:
                a += 1
                temp[guess[i]] -= 1
                res[i] = 0

        for i in range(4):
            if res[i] in temp:
                if temp[guess[i]] > 0:
                    b += 1
                    temp[guess[i]] -= 1
        return [a,b]



s = Solution()
solution="RGBY"
guess=   "GGRR"
print(s.masterMind(solution,guess))