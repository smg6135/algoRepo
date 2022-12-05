from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        # idea : for [..., num[j], num[i]] to exist, there must be at least one number num[k]
        # such that num[i] - num[j] == num[j] - num[k]
        # To keep track of these difference and number of this difference behind specific num[j]
        # we use DP
        # DP will store {difference between num[i] - num[j] : number of other number in nums that have 
        # same difference as the key behind num[j]}

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                res += dp[j][diff]
                # simple addding the DP will add the combination
                # for the example [2, 4, 6, 8, 10]
                # reaching 6, it'll add one since 4 has one element behind with one 2 diff
                # ex) 2, 4, 6 is added
                # reaching 8, itll add two since there are 2 elements behind 6 that has difference of 2
                # ex) on reaching 8, it'll add 2
                # 2, 4, 6, 8 and 4, 6, 8
                
                dp[i][diff] += dp[j][diff] + 1

                # since we acknowledged that nums[i] - num[j] also exists on the previous num list
                # we add one to the dp[j][diff] and add it on dp[i][diff] for later usage of the DP
                # ex) on reaching 10, the DP knows there are 3 elements behind 8 that has difference of 2
        return res


