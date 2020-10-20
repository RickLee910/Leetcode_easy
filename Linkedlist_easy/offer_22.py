class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        a = head
        b= head
        for i in range(k):
            a = a.next
        while a:
            a = a.next
            b = b.next
        return b