from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        max_row = len(grid)
        max_col = len(grid[0]) - 1
        for i in range(max_col + 1):
            stuck = False
            curr = [0, i]
            while curr[0] <= max_row - 1:
                # take adjacent cell
                curr_grid = grid[curr[0]][curr[1]]
                adjacent_grid = 0
                if curr_grid > 0 and curr[1] != max_col:
                    adjacent_grid = grid[curr[0]][curr[1] + 1]
                elif curr_grid < 0 and curr[1] != 0:
                    adjacent_grid = grid[curr[0]][curr[1] - 1]
                else:
                    stuck = True
                    break
                
                if curr_grid + adjacent_grid != 0:
                    curr[0] = curr[0] + 1
                    curr[1] = curr[1] + curr_grid
                else:
                    stuck = True
                    break
            if stuck:
                ans.append(-1)
            else:
                ans.append(curr[1])
        return ans
            
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Solution().findBall(grid)