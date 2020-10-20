def reverseList(self, head: ListNode) -> ListNode:
    temp = []

    def build(node):
        if not node:
            return
        temp.append(node.val)
        build(node.next)

    build(head)
    ans = ListNode()
    prev = ans
    for i in range(len(temp)):
        ans.next = ListNode(temp[-i - 1])
        ans = ans.next
    return prev.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1 = None      #前一个节点指针
        p2 = head   #当前节点指针
        while p2:
            tmp = p2.next  #临时存储当前节点指针的下一位
            p2.next = p1  #反转
            p1 = p2       #前一个节点指针后移一位
            p2 = tmp  #当前节点指针后移一位
        return p1
