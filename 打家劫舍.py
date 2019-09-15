#打家劫舍
#2019-08-13 05:29:16


class Solution(object):
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]
        if len(nums)==2:return max(nums)
        
        memo = [0]*len(nums) #memo[i] 表示偷到第i家最大收益
        for idx,num in enumerate(nums):
            if idx==0:
                memo[idx]=num
            elif idx==1:
                memo[idx]=max(num,memo[0])
            else:
                memo[idx]=max(memo[idx-1],memo[idx-2]+num)
                
        return memo[-1]
        