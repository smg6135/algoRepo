class Solution:
    def checkNeighbors(self, board, i, j):
        """
        return number of live cell around the board[i][j]
        """
        m = len(board)
        n = len(board[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        liveCt = 0
        for nb in neighbors:
            if 0 <= i + nb[0] < m and 0 <= j + nb[1] < n:
                if board[i + nb[0]][j + nb[1]] == 1:
                    liveCt += 1
        return liveCt

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        liveTranspo = []
        deadTrnaspo = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                nbCt =  self.checkNeighbors(board, i, j)
                if board[i][j] == 0:
                    if nbCt == 3:
                        deadTrnaspo.append((i, j))
                elif board[i][j] == 1:
                    if 2 > nbCt or nbCt > 3:
                        liveTranspo.append((i, j))
        
        for i, j in liveTranspo:
            board[i][j] = 0
        for i, j in deadTrnaspo:
            board[i][j] = 1
