class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        temp = []
        def search(l):
            if not l:
                return
            temp.append(l.val)
            search(l.next)
        search(head)
        return temp[-k]