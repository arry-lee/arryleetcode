#三维形体投影面积
#2019-01-12 20:41:55

class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum=0
        for row in grid:
            sum+=max(row)
            sum-=row.count(0)
        for col in zip(*grid):
            sum+=max(col)
        return sum+len(grid)*len(grid)