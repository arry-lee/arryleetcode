#��תͼ��
#2019-08-13 00:05:45

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # ����Ϊn ���� n//2 ��Ҫ��ת
        
        # �� i �� ���� n-i*2 ���з�Χ [i,n-i)
        
        # ת����i��
            # ���ĸ��ǿ�ʼ ����Ϊ[(i,i),(n-i-1,i),(n-i-1,n-i-1),(i,n-i-1)]
            
            # ˳ʱ��ѭ�������������� (1,0) (0,1) (-1,0) (0,-1)
            
        n = len(matrix)
        
        for i in range(n//2):# ������
            for j in range(i,n-i-1): #������
                # ��
                matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i] =\
                matrix[n-1-j][i],matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j]