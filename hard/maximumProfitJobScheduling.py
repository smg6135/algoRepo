from bisect import bisect_left
from functools import lru_cache
from typing import List


# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

#         # DP attempt wrong

#         n = max(endTime)

#         dp = [0 for i in range(n + 1)]

#         jobs = sorted(zip(startTime, endTime, profit))


#         max_profit = 0

#         for job in jobs:
#             if dp[job[0]] == 0:
#                 dp[job[1]] = max(dp[:job[0]]) + job[2]
#                 max_profit = max(dp[job[1]], max_profit)
#             else:
#                 dp[job[1]] += dp[job[0]] + job[2]
#                 max_profit = max(dp[job[1]], max_profit)
        
#         return max_profit

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        startTime.sort()

        @lru_cache(None)
        # i refers to the current job index in jobs
        def rec(i):
            # choose the next valid one
            # skip to the next one
            # maximum of those two
            if i == n:
                return 0
            
            # return the left most position such that element jobs[j][1]
            # join the startTime list, without messing up the sort
            j = bisect_left(startTime, jobs[i][1])

            # this will return the next startTime job after this jobs[j] finishes

            # choose this one and the next valid one
            one = jobs[i][2] + rec(j)

            # skip this one and straight to next one
            two = rec(i+1)

            return max(one, two)
        
        return rec(0)
    
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
print(Solution().jobScheduling(startTime, endTime, profit))