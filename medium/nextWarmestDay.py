from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use of monotone stack (descending)
        # each pop is the day we have to wait to go up
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        
        return ans

            
            

        # # TLE
        # n = len(temperatures)
        # i = 0
        # ans = []
        # for index, temp in enumerate(temperatures):
        #     i = index
        #     ct = 0
        #     while temperatures[i] <= temp:
        #         i += 1
        #         ct += 1
        #         if i == n:
        #             break
            
        #     if i == n:
        #         ans.append(0)
        #     else:
        #         ans.append(ct)
        
        # return ans

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))