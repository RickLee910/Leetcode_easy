class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        size = len(arr)
        count = 0
        for i in range(size):
            for j in range(i+1, size):
                if abs(arr[i]-arr[j]) <= a:
                    for k in range(j + 1, size):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1

        return count

a = [3,0,1,1,9,7]
sol = Solution()
print(sol.countGoodTriplets(a,7,2,3))