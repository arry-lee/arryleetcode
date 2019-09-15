#两个数组的交集
#2019-07-25 09:55:24

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))
        # return list(set(x for x in nums1 if x in nums2))