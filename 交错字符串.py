#½»´í×Ö·û´®
#2019-08-02 06:06:27

from functools import lru_cache
class Solution:
    @lru_cache()
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 
        if len(s1)==0:
            return s2==s3
        elif len(s2)==0:
            return s1==s3
        else:
            if s1[-1] == s3[-1] and s2[-1] == s3[-1]:
                return self.isInterleave(s1[:-1],s2,s3[:-1]) or self.isInterleave(s1,s2[:-1],s3[:-1])
            elif s1[-1] == s3[-1]:
                return self.isInterleave(s1[:-1],s2,s3[:-1])
            elif s2[-1] == s3[-1]:
                return self.isInterleave(s1,s2[:-1],s3[:-1])
            else:
                return False