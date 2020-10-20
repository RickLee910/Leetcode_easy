class Solution:
    def maxDistToClosest(self, seats):
        left = 0
        found_left = False

        max_len = 0
        for i in range(len(seats)):
            if seats[i] == 0 and not found_left:
                left = i
                found_left = True
            if seats[i] == 1 and found_left:
                if left == 0:
                    max_len = i - left
                else:
                    max_len = max((i - left + 1)// 2 , max_len)
                left = i + 1
                found_left = False
            if i == len(seats) - 1 and found_left:
                return max(i - left + 1, max_len)
        return max_len
s = Solution()
a = [1,0,0]
print(s.maxDistToClosest(a))
