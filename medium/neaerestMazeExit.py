from typing import List
from collections import deque
# both works but the first one is better (better runtime)
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ### Get the maze size, used later to check whether the neighbor is valid.
        m,n = len(maze),len(maze[0])
        
        ### The directions that we can go at each position.
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        ### We use deque to make the pop more efficient
        ### We also have the steps stored at each position, and at any time, 
        ### if we see an exit, we simply return the steps.
        ### Note that if you don't put the steps along with the positions, 
        ### you will need to keep track of the levels you are at during the search (see style2).
        q = deque([[entrance[0],entrance[1],0]])
        
        ### We don't need to use extra space to store the visited positions, 
        ### since we can directly change the empty position in the maze to a wall.
        maze[entrance[0]][entrance[1]] = '+'
        
        ### Doing a regular BFS search using deque; if there is anything left in the q, we will keep doing the search
        while q:
            ### Pop form left of the q,
            ### Since we have steps stored at each position, we don't need to make a loop here (see style2 for the loop version).
            xo,yo,steps = q.popleft()
            
            ### Check if the current location is an exit, and make sure it is not the entrance.
            if (0 in [xo,yo] or xo==m-1 or yo==n-1) and [xo,yo]!=entrance:
                return steps
            
            ### We go in four directions.
            for xn,yn in directions:
                x,y = xo+xn,yo+yn
                ### Make sure the new location is still inside the maze and empty.
                if 0<=x<m and 0<=y<n and maze[x][y]=='.':
                    ### We make the empty space into a wall, so we don't visit it in the future.
                    maze[x][y] = '+'
                    ### We need to increase the steps.
                    q.append([x,y,steps+1])
        
        ### If we don't find the result in BFS, we need to return -1
        return -1

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        moves = [(1, 0), (-1,0), (0, 1), (0, -1)]
        # BFS approach
        min_step = float('inf')
        queue = deque()
        queue.append(entrance)

        step_tracker = 0
        while queue:
            temp_q = deque()
            step_tracker += 1
            while queue:
                next_move = queue.popleft()
                maze[next_move[0]][next_move[1]] = '+'
                for move in moves:
                    moved_y = next_move[0] + move[0]
                    moved_x = next_move[1] + move[1]
                    if 0 <= moved_x < m and 0 <= moved_y < n and maze[moved_y][moved_x] != '+':
                        if moved_y == 0 or moved_x == 0 or moved_y == n - 1 or moved_x == m - 1:
                            return step_tracker
                        else:
                            temp_q.append([moved_y, moved_x])
            queue.extend(temp_q)
        return -1

maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".",".",".","+"],["+","+","+","+",".","+","."]]
entrance = [0,1]
print(Solution().nearestExit(maze, entrance))