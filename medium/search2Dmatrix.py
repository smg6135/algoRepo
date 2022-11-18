class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix[0])
        n = len(matrix)
        
        l = 0
        r = len(matrix)-1
        
        def helper(l,r):
            mid = l + ((r-l)//2)
            
            if target <= matrix[mid][0]: # target smaller than first item in list
                return helper(l, mid-1)
            
            elif target >= matrix[mid][m-1]: # target larger than last item in list
                return helper(mid + 1, r)
            
            else: #target within this row 
                for num in matrix[mid]:
                    if num == target:
                        return True
                return False
        
        return helper(l,r)

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))