#ֻ����һ�ε�����III
#2019-08-17 19:47:58

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        ˼·, ��ȫ�����һ��, �õ��Ľ��, �������ĳ����0λ(������߷�0λ), 
        ��ôֻ����һ�ε���������, �����λ��һ��Ϊ0, һ��Ϊ1, 
        �ɴ˿��Խ������е�Ԫ�طֳ�������,���±���, ���������ֵ
        """
        
        acc = 0
        for i in nums:
            acc ^= i
        
        a,b = 0,0
        n = 0
        while True:
            if (acc>>n)&1:
                break
            else:
                n+=1
                
        for i in nums:
            if i>>n&1:
                a^=i
            else:
                b^=i
        
        return a,b