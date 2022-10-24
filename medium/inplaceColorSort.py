class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        i = 0
        while(i < len(nums)-1):
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
                i = start
            elif nums[i] == 2 and end > i:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1

nums = [1, 0]
Solution().sortColors(nums)