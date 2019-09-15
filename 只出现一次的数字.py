#只出现一次的数字
#2019-08-12 21:00:28

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = nums[0]
        for num in nums[1:]:
            single ^= num
        return single