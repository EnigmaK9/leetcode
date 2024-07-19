# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        s = head
        q = head
        while q is not None and q.next is not None:
            s = s.next
            q = q.next.next
            if q == s:
                return True

        return False

