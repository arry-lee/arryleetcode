#旋转图像
#2019-08-13 00:05:45

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 长度为n 则有 n//2 层要旋转
        
        # 第 i 层 长度 n-i*2 行列范围 [i,n-i)
        
        # 转动第i层
            # 从四个角开始 坐标为[(i,i),(n-i-1,i),(n-i-1,n-i-1),(i,n-i-1)]
            
            # 顺时针循环各边坐标增量 (1,0) (0,1) (-1,0) (0,-1)
            
        n = len(matrix)
        
        for i in range(n//2):# 层坐标
            for j in range(i,n-i-1): #列坐标
                # 角
                matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i] =\
                matrix[n-1-j][i],matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j]