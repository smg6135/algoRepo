class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1

        hash_int = [0 for i in range(n)]
        for num in nums:
            if num > 0 and num <= n:
                hash_int[num - 1] = 1
        
        for i in range(n):
            if hash_int[i] == 0:
                return i + 1
        # if hash_int is not touched or everything is 1
        if hash_int[n-1] == 0:
            return 1
        else:
            return n + 1

Solution().firstMissingPositive([2,1])