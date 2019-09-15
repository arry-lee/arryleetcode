#È±Ê§Êý×Ö
#2019-08-13 07:03:07

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)//2-sum(nums)
        