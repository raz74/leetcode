# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse_node = []

        if head is None or head.next is None:
            return head

        p = head
        while p.next:
            n = p.next
            p.next = n.next
            n.next = head
            head = n
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

x = (Solution().reverseList(head))
print(x)
