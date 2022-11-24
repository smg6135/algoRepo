from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check 3 by 3
        three_by_three = [[1, 1], [1, 4], [1, 7], [4, 1], [4, 4], [4, 7], [7, 1], [7, 4], [7, 7]]
        around_coord = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for tc in three_by_three:
            hash_checker = defaultdict(int)
            init_bd = board[tc[0]][tc[1]]
            if init_bd != ".":
                hash_checker[init_bd] += 1
            for ac in around_coord:
                bd = board[tc[0] + ac[0]][tc[1] + ac[1]]
                if bd != ".":
                    hash_checker[bd] += 1
                    if hash_checker[bd] > 1:
                        return False

        # check row and col
        i = 0
        while i < 9:
            hash_checker = defaultdict(int)
            for j in range(0, 9):
                bd = board[i][j]
                if bd != ".":
                    hash_checker[bd] += 1
                    if hash_checker[bd] > 1:
                        return False

            hash_checker = defaultdict(int)
            for j in range(0, 9):
                bd = board[j][i]
                if bd != ".":
                    hash_checker[bd] += 1
                    if hash_checker[bd] > 1:
                        return False
            i += 1
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))