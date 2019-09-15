#����ˮ����
#2019-01-12 22:44:02

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # û��Ҫģ�����ջ��ֻ��Ҫ��������
        f, t = 0, 0 
        for b in bills:
            if b == 5:
                f += 1
            elif b == 10:
                if f == 0:
                    return False
                f -= 1
                t += 1    
            else:              
                if t and f:
                    t -= 1
                    f -= 1                     
                elif f >= 3:
                    f -= 3                     
                else:
                    return False
        return True
