from typing import ListNode
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slower = head             # faster iterates 2 times faster than slower.
                                  # if faster catches slower, then it is a cycle!
        faster = head.next
        
        while slower != faster:
            
            if slower is None or faster is None:
                return False
            if faster.next is None:
                return False
            slower = slower.next
            faster = faster.next.next
        
        return True