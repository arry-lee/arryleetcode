#移动零
#2019-08-12 21:19:12

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 第一次遇到非零元素，将非零元素与数组nums[0]互换，第二次遇到非零元素，将非零元素与nums[1]互换
        l = c = 0
        while l < len(nums):
            if nums[l] == 0:
                l += 1  
            else:
                nums[l],nums[c] = nums[c],nums[l]
                l += 1
                c += 1
                