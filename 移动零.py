#�ƶ���
#2019-08-12 21:19:12

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ��һ����������Ԫ�أ�������Ԫ��������nums[0]�������ڶ�����������Ԫ�أ�������Ԫ����nums[1]����
        l = c = 0
        while l < len(nums):
            if nums[l] == 0:
                l += 1  
            else:
                nums[l],nums[c] = nums[c],nums[l]
                l += 1
                c += 1
                