class Solution:
    class Solution:
        def isLongPressedName(self, name, typed):
            i, j = 0, 0
            n, m = len(name), len(typed)
            # 开始第一个进行判断
            if name[i] != typed[j]:
                return False
            # 进入循环，如果name[i]==typed[j]，那么指针同时指向第二个值，如果不等则判断typed的值是否和
            # name前一个值相等，如果相等，则typed指针向后移，如果不等则False
            while i < n and j < m:
                if name[i] == typed[j]:
                    i += 1
                    j += 1
                else:
                    if typed[j] == name[i - 1]:
                        j += 1
                    else:
                        return False
            # 退出循环如果name,typed刚好结束判断
            if i == n and j == m:
                return True
            # 退出循环，如果typed刚好结束而name没结束，说明name后还有字符
            if i < n:
                return False
            # 退出循环，如果name刚好结束而typed没结束，判断typed后面的字符是否和name最后一个字符相等
            if j < m:
                if ''.join(set(typed[j:])) == typed[j]:
                    return True
                return False

s = Solution()
a = "vzi"
b = "vvzz"
print(s.isLongPressedName(a,b))
