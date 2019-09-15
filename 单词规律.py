#µ¥´Ê¹æÂÉ
#2019-07-25 11:01:28

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split()
        p = list(pattern)
        if len(s)!=len(p):
            return False
        sp = [ x+y for x,y in zip(s,p)]
        return len(set(s))==len(set(p)) and len(set(s))==len(set(sp))
            