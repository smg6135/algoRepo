# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # # intuitive solution
    #     # track_max = 0
    #     # curr_node = head
    #     # while curr_node:
    #     #     curr_node = curr_node.next
    #     #     track_max += 1
        
    #     # track_max = math.floor(track_max / 2)

    #     # res_node = head
    #     # for i in range(track_max):
    #     #     res_node = res_node.next
        
    #     # return res_node
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # better solution
        #two poiters: slow and fast
        #while one pointer goes from 2 by 2, the slow goes 1 by 1

        #both start at the same point
        slow = head
        fast = head

        #while we have both fast and fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow