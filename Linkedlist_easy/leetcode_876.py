class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = []
        prev = head
        while prev:
            temp.append(prev.val)
            prev = prev.next
        mid = len(temp) // 2
        prev = head
        for i in range(mid):
            prev = prev.next
        return prev

    class Solution:
        def middleNode(self, head: ListNode) -> ListNode:
            fast, slow = head, head
            while fast:
                fast = fast.next
                if not fast: break
                slow = slow.next
                fast = fast.next
            return slow