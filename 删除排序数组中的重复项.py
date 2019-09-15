#删除排序数组中的重复项
#2019-08-12 20:27:11

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 你不需要考虑数组中超出新长度后面的元素。
        if not nums:return 0
        
        len_nums = len(nums)
        i = 0
        j = 1
        for j in range(1,len_nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i+1