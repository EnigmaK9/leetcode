# Creation Date: 2026-05-09
# Last Modified: 2026-05-09
# Description: detect cycle in a linked list using floyd's cycle-finding algorithm
# Author: Carlos


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False
