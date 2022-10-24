# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional) -> Optional:
        if head is None:
            return head
        current = head
        nxt = head.next
        while nxt is not None:
            if current.val == nxt.val:
                current.next = nxt.next
                nxt = current  # If there are more than two same elements we will check them again
            current = nxt
            nxt = nxt.next
        return head
