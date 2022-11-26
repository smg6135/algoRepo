from typing import List


# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         # np solution
#         # TLE
#         n = len(arr)
#         init_sum = 0
#         dp = [[0 for i in range(n)] for i in range(n)]

#         # initial
#         for i in range(n):
#             dp[i][i] = arr[i]
#             init_sum += arr[i]

#         # follow
#         for k in range(n-1, 0, -1):
#             for i in range(k):
#                 j = n - k + i
#                 dp[i][j] = min(dp[i][j - 1], dp[i + 1][j])
#                 init_sum += dp[i][j]

#         return init_sum

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack = [-1]
        res = 0
        for i2, n in enumerate(arr):
            while stack and n < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]
                left = index - i1
                right = i2 - index
                res += (arr[index] * left * right)
            stack.append(i2)
        return res % (10**9 + 7)

print(Solution().sumSubarrayMins([3, 1, 2, 4]))