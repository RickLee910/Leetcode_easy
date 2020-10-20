class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        temp = [0] * num_people
        count = 1
        while candies != 0:
            for i in range(num_people):
                if candies < count:
                    temp[i] += candies
                    candies = 0
                    break
                temp[i] += count 
                candies -= count
                count += 1
        return temp
s = Solution()
a = 7
b = 4
print(s.distributeCandies(a,b))