#位1的个数
#2019-08-13 06:45:50

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            n >>= 1
        return cnt