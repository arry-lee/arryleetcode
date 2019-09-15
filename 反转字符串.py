#·´×ª×Ö·û´®
#2019-08-13 00:15:46

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # l,r = 0,len(s)-1
        # while l<r:
        #     s[r],s[l] = s[l],s[r]
        #     l += 1
        #     r -= 1
        #
        s.reverse()