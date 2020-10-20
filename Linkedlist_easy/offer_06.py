
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        temp = []
        while head:
            temp.append(head.val)
            head =head.next
        return temp[::-1]