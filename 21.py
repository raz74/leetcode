# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mereged_list = None
        tail = None

        while list1 is not None or list2 is not None:
            if list1 is None:
                node = ListNode(list2.val)
                list2 = list2.next
            elif list2 is None:
                node = ListNode(list1.val)
                list1 = list1.next
            elif list1.val < list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next

            if tail is None:
                tail = node
                mereged_list = tail
            else:
                tail.next = node
                tail = node

        return mereged_list


l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(10)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

x = Solution().mergeTwoLists(l1, l2)
print(x)