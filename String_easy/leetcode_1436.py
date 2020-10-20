class Solution:
    def destCity(self, paths) -> str:
        dic = {}
        for i in range(len(paths)):
            dic[paths[i][0]] = paths[i][1]
        value = list(dic.values())
        keys = list(dic.keys())
        for i in value:
            if i not in keys:
                return i
s =Solution()
a = [["B","C"]]
print(s.destCity(a))