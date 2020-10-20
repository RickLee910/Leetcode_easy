class Solution:
    def constructRectangle(self, area: int):
        mind = {}
        for i in range(1,int(area**0.5)+1):
            if area % i == 0:
                mind[area//i - i] = i
        return [area // mind[min(mind.keys())],mind[min(mind.keys())]]
s = Solution()
a= 122122
print(s.constructRectangle(a))