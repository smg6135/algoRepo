import heapq
from typing import List


class Solution:
    
    def maxPerformance(self, n, speed, efficiency, k):
        """
        Using heap, add the engineer with the most efficiency first 
        remove from heap from the head aka the engineer with the least speed 
        """
        h = []
        res = sSum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(h, s)
            sSum += s
            if len(h) > k:
                sSum -= heapq.heappop(h)
            res = max(res, sSum * e)
        return res % (10**9 + 7)



n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
for e, s in sorted(zip(efficiency, speed), reverse=1):
    print((e, s))
Solution().maxPerformance(n, speed, efficiency, k)