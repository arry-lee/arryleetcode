#��ƽ���ǹ�����
#2019-07-30 22:53:42

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:

        dev = (sum(A)-sum(B))/2
        # for a in A:
        #     for b in B:
        #         if a-b == de:
        #             return a,b
        # O(nn)��ʱ��
        # ���Ͽ�һ��
        # ����������ȥ��
        setB = set(B)
        for a in A:
            b = a-dev
            if a-dev in setB:
                return [a,b]