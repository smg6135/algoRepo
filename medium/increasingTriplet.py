from ast import List
import math


class Solution:
    def increasingTriplet(self, nums) -> bool:
        # greedy approach
        # As we proceed, if there's minimum, and there's a number in between and the number that's bigger than both
        # then it's a solution
        minimum = math.inf
        mid = math.inf
        for num in nums:
            if num < minimum:
                minimum = num
            elif minimum < num < mid:
                mid = num
            else:
                if(num > mid):
                    return True
        return False
print(Solution().increasingTriplet([20,100,10,12,5,13]))