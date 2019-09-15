#È«ÅÅÁĞII
#2019-04-02 16:23:59


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools

        ss = itertools.permutations(nums)

        return list(set(ss))