#����֮��
#2019-08-12 21:54:31

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ����һ���������� ���ַ� �����˳��
        # Ӧ����ͨ��ֵ�����
        h = {}
        for i, num in enumerate(nums):
            if (target - num) in h:
                return [i, h[target - num]]
            h[num] = i
        