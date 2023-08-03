from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # end condition
        if len(nums) == 1:
            return [nums[:]]
        
        # for each element, pop the first element, get the permutations from the rest
        # of the element, append the popped element into the permutations you got from
        # the rest of the element, add that to result

        for i in range(len(nums)):
            temp = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(temp)
            
            res.extend(perms)
            nums.append(temp)
        
        return res

Solution().permute([1, 2, 3])