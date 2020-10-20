class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = []

        def add(node):
            if node:
                temp.append(node.val)
                add(node.next)

        add(head)

        return temp == temp[::-1]