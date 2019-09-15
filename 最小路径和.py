#最小路径和
#2019-08-17 04:29:11

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        dp = [[0 for i in range(cols)] for j in range(rows)]
        
        # dp[i][j] 表示从 (0,0) 到 (i,j) 的最小路径和
        
        for i in range(rows):
            for j in range(cols):
                if i>0 and j>0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
                elif i==0 and j==0:
                    dp[i][j] = grid[i][j]
                
                elif i==0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
        
        return dp[-1][-1]