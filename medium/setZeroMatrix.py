from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Grab rows and column value
        matrixRow = len(matrix)
        matrixCol = len(matrix[0])
        # get "markers" (i, j position of 0 array) for later 0 conversion
        setMarker = []
        for i in range(matrixRow):
            for j in range(matrixCol):
                if matrix[i][j] == 0:
                    setMarker.append((i, j))

        # for each marker, change that whole row with 0 and using the column value
        # iterate through each row and covert the column w zero
        for marker in setMarker:
            matrix[marker[0]] = [0] * matrixCol
            for rownum in range(matrixRow):
                matrix[rownum][marker[1]] = 0
        


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solutionObj = Solution()
solutionObj.setZeroes(matrix)
print(matrix)
        
        