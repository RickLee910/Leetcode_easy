class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        temp = head
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
                return head
            temp = temp.next
