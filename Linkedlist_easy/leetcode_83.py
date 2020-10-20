class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nex = head.next
        prev = head
        while nex:
            if head.val == nex.val:

                head.next = nex.next
                nex = head.next
            else:
                nex = nex.next
                head = head.next
        return prev
