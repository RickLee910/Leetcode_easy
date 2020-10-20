class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ''
        for i in range(len(address)):
            if address[i].isdigit():
                ans += address[i]
            else:
                ans += '[.]'
        return ans
