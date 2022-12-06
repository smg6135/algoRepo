class Solution(object):
    # def sortColors(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     start = 0
    #     end = len(nums) - 1
    #     i = 0
    #     while(i < len(nums)-1):
    #         if nums[i] == 0:
    #             nums[start], nums[i] = nums[i], nums[start]
    #             start += 1
    #             i = start
    #         elif nums[i] == 2 and end > i:
    #             nums[end], nums[i] = nums[i], nums[end]
    #             end -= 1
    #         else:
    #             i += 1
    # slightly faster 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        b = len(nums) - 1
        i = 0
        while i <= b:
            if nums[i] == 0:
                nums[r], nums[i] = nums[i], nums[r]
                r += 1
                if nums[i] == 0:
                    i += 1
            elif nums[i] == 2:
                nums[b], nums[i] = nums[i], nums[b]
                b -= 1
            else:
                i += 1

nums = [1, 0]
Solution().sortColors(nums)