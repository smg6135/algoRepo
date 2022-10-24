from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
         # start hopping from Node_#0
        slow, fast = 0, 0
		
		# for locating start node of cycle
        check = 0
        
		# Step_#1
		# Cycle detection
        # Let slow jumper and fast jumper meet somewhere in the cycle 
		
        while True:
            
			# slow jumper hops 1 step, while fast jumper hops two steps forward.
            slow = nums[ slow ]
            fast = nums[ nums[fast] ]
            
            if slow == fast:
                break
        
		
		# Step_#2
        # Locate the start node of cycle (i.e., the duplicate number)
        while True:
            
            slow = nums[ slow ]
            check = nums[ check ]
            
            if slow == check:
                break
        
        return check

Solution().findDuplicate([1,2,4,3,3])