# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        trackA = headA
        trackB = headB
        # range of 3 since there's 3 possible way that the end meets
        # trackA reached the end of a linked list
        # trackB reached the end of a linked list
        # third time no hit == no intersection
        for _ in range(3):
            while trackA and trackB:
                if trackA == trackB:
                    return trackA
                trackA = trackA.next
                trackB = trackB.next
            if trackA is None:
                trackA = headB
            if trackB is None:
                trackB = headA
        return None