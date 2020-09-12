class Solution:
    def rotate1(self, nums, k):
        temp = [0] * k
        temp.extend(nums)
        for i in range(k):
            temp[k-i - 1] = temp[-1]
            temp.pop()
        return temp

    def rotate2(self, nums, k):
        temp = [0] * len(nums)
        for i in range(len(nums)):
            temp[(i + k) % len(nums)] = nums[i]
        return temp

    def rotate(self, nums, k):
        n = len(nums)
        start = 0
        count = 0
        while count != n:
            curr_idx = start  # 从索引curr_idx开始，将它的值赋给索引(curr_idx + k) % n
            curr_val = nums[start]
            while True:
                next_idx = (curr_idx + k) % n
                temp = nums[next_idx]
                nums[next_idx] = curr_val
                curr_val = temp
                curr_idx = next_idx
                count += 1  # 整个数组只需要n次赋值就可以了，所以count==n
                if curr_idx == start:
                    start += 1  # 从start出发又回到了start，如果count小于n则从start+1处继续开始
                    break
        return nums


s = Solution()
a = [1,2,3,4,5,6,7]
print(s.rotate(a, 3))