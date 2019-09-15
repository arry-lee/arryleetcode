#有效的字母异位词
#2019-08-13 00:48:58

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):return False
        # list_s = list(s)
        # list_s.sort()
        # list_t = list(t)
        # list_t.sort()
        # return list_s == list_t
        return collections.Counter(s)==collections.Counter(t)