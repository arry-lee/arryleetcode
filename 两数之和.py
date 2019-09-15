#两数之和
#2019-08-12 21:54:31

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 这是一个查找问题 二分法 会打乱顺序
        # 应该是通过值反查键
        h = {}
        for i, num in enumerate(nums):
            if (target - num) in h:
                return [i, h[target - num]]
            h[num] = i
        