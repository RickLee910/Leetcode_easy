class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        ans = 0
        for i in range(len(temp)):
            if temp[-i-1] == 1:
                ans += 2 ** i
        return ans