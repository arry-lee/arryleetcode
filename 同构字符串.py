#Í¬¹¹×Ö·û´®
#2019-01-07 21:12:13

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        