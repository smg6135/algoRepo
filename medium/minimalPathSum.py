from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        dp = [[0 for _ in range(c)] for _ in range(r)]
        
        dp[0][0] = grid[0][0]

        for i in range(1, c):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        
        for i in range(1, r):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[r-1][c-1]