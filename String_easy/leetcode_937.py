class Solution:
    def reorderLogFiles1(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)



    def reorderLogFiles(self, logs):
        let = []
        dig = []

        for i in logs:
            if i[-1].isalpha():
                let.append(i)
            else:
                dig.append(i)




        let.sort(key = lambda s:s.split()[0])
        let.sort(key=lambda s: s.split()[1:])
        return let + dig
s = Solution()
a = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(s.reorderLogFiles(a))