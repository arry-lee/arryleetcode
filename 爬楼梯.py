#ÅÀÂ¥ÌÝ
#2019-08-13 04:10:50

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b = 1,1
        
        while n:
            a,b = b,a+b
            n -= 1
            
        return a