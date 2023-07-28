from collections import deque
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        starting_pos = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if (i + nums[i]) >= starting_pos:
                starting_pos = i
        
        return starting_pos == 0
Solution().canJump([2,3,1,1,4])