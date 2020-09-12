class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        Sum = sum(distance)
        if start < destination:
            len_1 = sum(distance[start:destination])
        else:
            len_1 = sum(distance[destination:start])

        return min(len_1,Sum - len_1)
s = Solution()
a =[7,10,1,12,11,14,5,0]
st = 7
de = 2
print(s.distanceBetweenBusStops(a,st,de))

