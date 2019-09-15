#¿ìÀÖÊý
#2019-01-07 20:30:41

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        m = 0
        while n:
            m += (n%10)**2
            n /= 10
               
        if m == 1:
            return True
        elif m == 4:
            return False
        else:
            return self.isHappy(m)