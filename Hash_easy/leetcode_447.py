class Solution:
    def numberOfBoomerangs(self, points) -> int:
        def distance(a,b):
            return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)

        ans = 0
        for i in range(len(points)):
            d = {}
            for j in range(len(points)):
                l = distance(points[i],points[j])
                if l in d.keys():
                    d[l] += 1
                else:
                    d[l] = 1
            for k in d.values():
                if k > 1:
                    ans += k * (k - 1)

        return ans
s = Solution()
a = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
print(s.numberOfBoomerangs(a))