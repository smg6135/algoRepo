from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # greedy + two pointers
        # have the left most and right most container side
        # move to left and right based on the height
        # prioritize length of the bar 
        # O(n)
        left, right = 0, len(height) - 1
        total_area = 0
        while left != right:
            if height[left] < height[right]:
                total_area = max(total_area, height[left] * (right - left))
                left += 1
            elif height[left] >= height[right]:
                total_area = max(total_area, height[right] * (right - left))
                right -= 1
        return total_area
