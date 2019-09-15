#第一个错误的版本
#2019-08-13 04:05:38

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        hi = n
        lo = 1
        
        # [0 1 1]
        while lo<hi:
            mid = (lo+hi)//2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid+1
        
        return lo
        