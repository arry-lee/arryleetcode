#有效的数独
#2019-08-12 23:01:35

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 一次扫描所有的
        # (key,pos) 元素和其位置对是唯一的
        # ('8',i) 行('8',j)列 ('8',b)块 区分
              
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