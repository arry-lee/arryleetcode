#¥Úº“ΩŸ…·II
#2019-01-14 20:08:03

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def robin(nums):
            last,now = 0, 0
            for n in nums:
                last, now = now, max(last+n,now)
            
            return now
        
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        return max(robin(nums[1:]),robin(nums[:-1]))