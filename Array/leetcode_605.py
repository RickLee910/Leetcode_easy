class Solution:
    #三连花种一盆花
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        flowerbed = [0]+ flowerbed
        flowerbed = flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            if  flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n = n-1
                flowerbed[i] = 1
        return n<=0
    #贪心算法
    def canPlaceFlowers1(self, flowerbed, n):
        left,right = 0, 0
        left_found = False
        count = 0
        size = len(flowerbed)
        if size == 1 and flowerbed[0] == 0 and n <= 1:
            return True
        for i in range(size):
            if flowerbed[i] == 0 and not left_found:
                left = i
                left_found = True
            elif flowerbed[i] == 1:
                right = i
                if left == 0:
                    if right - left >= 2:
                        count += (right - left) // 2
                        left_found = False
                        left = right + 1
                if right - left >= 3:
                    count += (right - left - 1) // 2
                    left = right + 1
                    left_found = False
                else:
                    left = right + 1
            elif i == size - 1:
                right = i + 1
                if left == 0:
                    count += (size + 1) // 2
                elif right - left >= 2:
                    count += (right - left) // 2
        if count >= n:
            return True
        return False
s = Solution()
a = [0,0]
print(s.canPlaceFlowers(a, 2))