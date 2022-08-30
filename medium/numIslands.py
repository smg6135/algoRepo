from collections import deque
from typing import List



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        island = 0
        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == "1":
                    # start of island
                    # do BFS and find the island end
                    grid[row][col] = "0"
                    adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    gridQ = deque()
                    gridQ.append((row, col))
                    # if found start of the island, append it to queue
                    # while looping the q, find the adjacent 1s and add it to the queue so you can
                    # expand it to find the island
                    # if the queue is empty and escapes it means it traversed all the adjacent 1s 
                    # hence the island is finished so add 1 to the answer when the queue ends
                    # also while looping change the 1s that was adjacent to 0 to indicate that the 1s are visited
                    # hence removing double counting islands
                    while gridQ:
                        currPair = gridQ.pop()
                        for pair in adj:
                            if 0 <= currPair[0]+pair[0] <= maxRow and 0 <= currPair[1]+pair[1] <= maxCol and  grid[currPair[0]+pair[0]][currPair[1]+pair[1]] == "1":
                                gridQ.append((currPair[0]+pair[0], currPair[1]+pair[1]))
                                grid[currPair[0]+pair[0]][currPair[1]+pair[1]] = "0"
                    island += 1

        return island


grid = [
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"]
]
print(Solution().numIslands(grid))