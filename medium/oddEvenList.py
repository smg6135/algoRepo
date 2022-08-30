# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        oddStart = odd
        even = ListNode()
        head = head[0]
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            if even is not None:
                head = head.next.next
            else:
                head = None
        
        odd.next = even
        
        return oddStart
    
Solution().oddEvenList([ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))])