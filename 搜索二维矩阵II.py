#ËÑË÷¶þÎ¬¾ØÕóII
#2019-08-11 03:22:12

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        r = len(matrix)
        c = len(matrix[0])
        
        i = 0
        j = c-1
        while i<r and j>=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
                
        return False