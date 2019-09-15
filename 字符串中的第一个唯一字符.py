#字符串中的第一个唯一字符
#2019-08-13 00:38:34

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for idx,letter in enumerate(s):
            if letter in d:
                d[letter]=None
            else:
                d[letter]=idx
        
        x = [v for v in d.values() if v is not None]
        if not x:
            return -1
        else:
            return min(x)
                