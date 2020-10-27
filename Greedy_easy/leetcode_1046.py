class Solution:
    def lastStoneWeight(self, stones) -> int:

        while len(stones) > 1:
            stones.sort()
            temp = abs(stones[-1] - stones[-2])
            stones = stones[:-2]
            stones.append(temp)
        return stones[0]