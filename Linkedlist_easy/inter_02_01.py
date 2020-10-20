class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp = set()
        temp.add(head.val)
        prev = head
        tool = head
        head = head.next

        while head:

            if head.val in temp:
                tool.next = head.next
                head = tool.next
            else:
                temp.add(head.val)
                head = head.next
                tool = tool.next

        return prev