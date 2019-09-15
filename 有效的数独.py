#��Ч������
#2019-08-12 23:01:35

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # һ��ɨ�����е�
        # (key,pos) Ԫ�غ���λ�ö���Ψһ��
        # ('8',i) ��('8',j)�� ('8',b)�� ����
              
        memo = set()
        for i,j in itertools.product(range(9),range(9)):
            v = board[i][j]

            if v != ".":
                check_list = [(v,i,-1),(v,-1,j),(v,i//3,j//3)]                   
                for item in check_list:
                    if item in memo:
                        return False
                    else:
                        memo.add(item)
        return True