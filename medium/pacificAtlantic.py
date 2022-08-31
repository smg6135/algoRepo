from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 1st approach
        # for each block if it reaches both pacific and atlantic
        # add as a res
        # problem: takes too long
        """
                for i in range(m):
            for j in range(n):
                visited = []
                nodeQ = deque()
                nodeQ.append([i, j])
                isAtalantic = False
                if j == n - 1 or i == m - 1:
                    isAtalantic = True
                isPacific = False
                if j == 0 or i == 0:
                    isPacific = True
                while nodeQ:
                    popQ = nodeQ.pop()
                    currH = heights[popQ[0]][popQ[1]]
                    for coord in adjacent:
                        if 0 <= popQ[0] + coord[0] < m and 0 <= popQ[1] + coord[1] < n and heights[popQ[0] + coord[0]][popQ[1] + coord[1]] <= currH and [popQ[0] + coord[0], popQ[1] + coord[1]] not in visited:
                            nodeQ.append([popQ[0] + coord[0], popQ[1] + coord[1]])
                            if popQ[0] + coord[0] == 0 or popQ[1] + coord[1] == 0:
                                isPacific = True
                            if popQ[0] + coord[0] == m - 1 or popQ[1] + coord[1] == n - 1:
                                isAtalantic = True
                if isAtalantic and isPacific:
                    res.append([i, j])
        """
        # the appropriate approach
        # take the squares that is connected to atalantic and pacific, lets say Asquares and Psqaures
        # using bfs get all the squares that is reachable by from Asquares and Psquares
        # from these squares if it repeats, it's the answer
        m = len(heights)
        n = len(heights[0])
        adjacent = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        Psquares = set([(i, 0) for i in range(m)] + [(0, j) for j in range(n)])
        Asquares = set([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)])
        Pqueue = deque(Psquares)
        while Pqueue:
            popQ = Pqueue.popleft()
            for coord in adjacent:
                if 0 <= popQ[0] + coord[0] < m and 0 <= popQ[1] + coord[1] < n and (popQ[0] + coord[0], popQ[1] + coord[1]) not in Psquares and heights[popQ[0] + coord[0]][popQ[1] + coord[1]] >= heights[popQ[0]][popQ[1]]:
                    Pqueue.append((popQ[0] + coord[0], popQ[1] + coord[1]))
                    Psquares.add((popQ[0] + coord[0], popQ[1] + coord[1]))
                    
        Aqueue = deque(Asquares)
        while Aqueue:
            popQ = Aqueue.popleft()
            for coord in adjacent:
                if 0 <= popQ[0] + coord[0] < m and 0 <= popQ[1] + coord[1] < n and (popQ[0] + coord[0], popQ[1] + coord[1]) not in Asquares and heights[popQ[0] + coord[0]][popQ[1] + coord[1]] >= heights[popQ[0]][popQ[1]]:
                    Aqueue.append((popQ[0] + coord[0], popQ[1] + coord[1]))
                    Asquares.add((popQ[0] + coord[0], popQ[1] + coord[1]))

        return list(Psquares & Asquares)

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
