#��������Ľ���II
#2019-08-12 21:08:26


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # l = list(set(nums1)&set(nums2))
        # res = []
        # for i in l:
        #     c = min(nums1.count(i),nums2.count(i))
        #     res.extend([i]*c)
        # return res
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

# ��������������Ѿ��ź����أ��㽫����Ż�����㷨��
# ��� nums1 �Ĵ�С�� nums2 С�ܶ࣬���ַ������ţ�
# ��� nums2 ��Ԫ�ش洢�ڴ����ϣ������ڴ������޵ģ������㲻��һ�μ������е�Ԫ�ص��ڴ��У������ô�죿
    