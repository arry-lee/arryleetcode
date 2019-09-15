#只出现一次的数字III
#2019-08-17 19:47:58

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        思路, 先全部异或一次, 得到的结果, 考察其的某个非0位(比如最高非0位), 
        那么只出现一次的两个数中, 在这个位上一个为0, 一个为1, 
        由此可以将数组中的元素分成两部分,重新遍历, 求两个异或值
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