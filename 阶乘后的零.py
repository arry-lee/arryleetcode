#�׳˺����
#2019-07-30 23:21:19

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # �ֽ������� 5�ĸ�������ĩβ0�ĸ��� 
        # 1 2 3 4|5 6 7 8 9| 10 11 12 13 14 |
        p = 0
        while n >= 5:
            n = n // 5
            p += n
        return p