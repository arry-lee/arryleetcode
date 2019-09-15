#Ðý×ªÊý×é
#2019-08-12 20:51:18

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        # 15%
        # while steps:
        #     nums.insert(0,nums.pop())
        #     steps -= 1
        
        right = nums[-k:]
        nums[k:] = nums[0:-k]
        nums[0:k] = right