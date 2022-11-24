from collections import deque
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find initial points
        # bfs each
        n = len(board)
        m = len(board[0])
        wn = len(word)
        queue = deque()
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    queue.append([i, j])
        
        surround = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = []
        word_pt = 1
        while queue and word_pt < wn:
            temp_q = deque()

            while queue:
                next_p = queue.popleft()

                for sur in surround:
                    next_r = next_p[0] - sur[0]
                    next_c = next_p[1] - sur[1]
                    if 0 <= next_r < n and 0 <= next_c < m:
                        if board[next_r][next_c] == word[word_pt] and [next_r, next_c] not in visited:
                            visited.append(next_p)
                            temp_q.append([next_r, next_c])

            queue.extend(temp_q)
            word_pt += 1

        if queue:
            return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        
        if len(word) > m * n: return False                            # [a] trivial case to discard

        if not (cnt := Counter(word)) <= Counter(chain(*board)):      # [b] there are not enough
            return False                                              #     letters on the board
        
        if cnt[word[0]] > cnt[word[-1]]:                              # [c] inverse word if it's better
             word = word[::-1]                                        #     to start from the end
        
        def dfs(i, j, s):                                             # recursive postfix search
            
            if s == len(word) : return True                           # [1] found the word
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[s]:  # [2] found a letter
                board[i][j] = "#"                                     # [3] mark as visited
                adj = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]               # [4] iterate over adjacent cells...
                dp = any(dfs(ii,jj,s+1) for ii,jj in adj)             # [5] ...and try next letter
                board[i][j] = word[s]                                 # [6] remove mark
                return dp                                             # [7] return search result

            return False                                              # [8] this DFS branch failed
                
        return any(dfs(i,j,0) for i,j in product(range(m),range(n)))

board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(Solution().exist(board, word))