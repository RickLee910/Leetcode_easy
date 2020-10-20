class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def jj(w):
            return bin(w).count('1')
        arr.sort()
        return sorted(arr, key=lambda x: jj(x))