import math
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax, curMin = 1, 1
        res = nums[0]
        
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
			
            res = max(res, curMax)
            
        return res
Solution().maxProduct([2, 3, -2, 4])