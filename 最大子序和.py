#��������
#2019-08-13 05:08:06

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # // Kadane�㷨ɨ��һ���������е�������ֵ��
        # // ��ÿһ��ɨ�������Ըõ���ֵΪ������������е����ͣ������ͣ���
        # // ������������������ɣ���ǰһ��λ��Ϊ���������������С���λ�õ���ֵ��
        # // ��Ϊ���㷨�õ��ˡ�����ӽṹ������ÿ��λ��Ϊ�յ����������ж��ǻ�����ǰһλ�õ���������м���ó�, 
        # // ���㷨�ɿ��ɶ�̬�滮��һ�����ӡ�
        # // ״̬ת�Ʒ��̣�sum[i] = max{sum[i-1]+a[i],a[i]}   
        # // ����(sum[i]��¼��a[i]Ϊ������ĩ�˵����������������)
        
        max_sofar = float('-inf')
        max_last = float('-inf')
        
        for num in nums:
            max_last = max(num,max_last+num)
            max_sofar = max(max_sofar,max_last)
        return max_sofar