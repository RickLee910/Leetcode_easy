from collections import Counter, deque
class Solution:
    def sortString(self, s: str) -> str:
        c = Counter(s)
        d = deque()
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in c:
                d.append([i,c[i]])
        res = ""
        while d:
            dd = deque()
            while d:
                item = d.popleft()
                res += item[0]
                if item[1] > 1:
                    dd.appendleft([item[0],item[1]-1])
            d = dd
        return res
    def sortString1(self, s: str) -> str:
        h = [0] * 26
        for ch in s:
            h[ord(ch) - 97] += 1

        def appendChar(ret, p):
            if h[p] > 0:
                h[p] -= 1
                ret.append(chr(p + 97))

        def haveChar():
            return any(h[i] > 0 for i in range(26))

        ret = list()
        while True:
            if not haveChar():
                break
            for i in range(26):
                appendChar(ret, i)
            for i in range(26):
                appendChar(ret, 25 - i)
        return "".join(ret)

s =Solution()
a = "aaaabbbbcccc"
print(s.sortString(a))