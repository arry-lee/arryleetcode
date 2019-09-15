#´æÔÚÖØ¸´ÔªËØ
#2019-08-12 20:55:21

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)