#只出现一次的数字II
#2018-12-25 17:04:31

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*sum(set(nums)) - sum(nums))/2