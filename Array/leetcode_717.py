class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        if len(bits) == 1:
            return True
        if len(bits) >= 2 and bits[-2] == 0:
            return True
        bits.pop()
        l = 0
        while l < len(bits):
            if l == len(bits) - 1:
                if bits[l] == 1:
                    return False
                return True
            if l == len(bits) - 2:
                if bits[l] == 1:
                    return True
                else:
                    l += 1
            if bits[l] == 1 and l < len(bits) - 2:
                l += 2
            elif bits[l] == 0 and l < len(bits) - 2:
                l += 1
