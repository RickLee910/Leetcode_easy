import collections
class Solution:
    #hashmap方式，将(a,b)or(b,a)映射为小数字在前大数在后的整数ab,然后遍历字典记录次数
    def numEquivDominoPairs(self, dominoes):
        size = len(dominoes)
        count = 0
        d = collections.defaultdict(int)
        for i, j in dominoes:
            num = 10 * i + j if i < j else 10 * j + i
            count += d[num]
            d[num] += 1
        return count
    #暴力法，可解但超时
    def numEquivDominoPairs1(self, dominoes):
        size = len(dominoes)
        count = 0
        for i in range(size - 1):
            for j in range(i+1, size):
                if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                    count += 1
                    continue
                if dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
                    count += 1
        return count
sol = Solution()
a = [[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]
print(sol.numEquivDominoPairs(a))
