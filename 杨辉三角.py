#Ñî»ÔÈý½Ç
#2018-12-25 21:47:48

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return[[1],[1,1]]
        
        else:
            g = self.generate(numRows-1)
            new = [1]
            for i in range(numRows-2):
                new.append(g[-1][i]+g[-1][i+1])
            new.append(1)
            g.append(new)
            return g