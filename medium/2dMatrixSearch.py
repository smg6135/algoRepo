from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        cols = len(matrix[0])

        def binarySearch(row, low, high, target):
            if low > high:
                return False
                
            mid = (high + low) // 2

            if row[mid] == target:
                return True

            if target < row[mid]:
                return binarySearch(row, low, mid-1, target)
            
            return binarySearch(row, mid+1, high, target)


        if matrix[0][0] > target:
            return False

        for i in range(1, row):
            if target < matrix[i][0]:
                return binarySearch(matrix[i-1], 0, cols-1, target)
        
        return binarySearch(matrix[row-1], 0, cols-1, target)
        