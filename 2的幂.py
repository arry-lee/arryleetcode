#2µÄÃİ
#2019-08-17 19:36:57

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n&(n-1)==0