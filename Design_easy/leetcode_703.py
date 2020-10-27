class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.n = nums

    def add(self, val: int) -> int:
        self.n.append(val)
        return sorted(self.n)[self.k-1]
