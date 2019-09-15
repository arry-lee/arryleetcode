#比特位计数
#2019-08-17 19:56:42

class Solution:
    def countBits(self, num: int) -> List[int]:
        
        res = [0]*(num+1)
        
        for i in range(1,num+1):
            if i&1:
                res[i] = res[i-1]+1
            else:
                res[i] = res[i>>1]
        
        return res
        