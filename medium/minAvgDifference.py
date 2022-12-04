from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        import math
        res = (float('inf'), 0)

        n = len(nums)
        left_sum = 0
        total = sum(nums)

        for i in range(n):
            left_sum += nums[i]
            s_h = total - left_sum
            f_h_avg = math.floor(sum(left_sum) / (i + 1))
            
            if n - (i + 1) != 0:
                s_h_avg = math.floor(sum(s_h) / (n - (i + 1)))
            else:
                s_h_avg = 0

            abs_min_diff = abs(f_h_avg - s_h_avg)

            if abs_min_diff < res[0]:
                res[0] = abs_min_diff
                res[1] = i
        
        return res[1]
    