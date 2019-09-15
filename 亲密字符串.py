#Ç×ÃÜ×Ö·û´®
#2019-01-12 22:06:48

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if A == B:
            if len(set(A)) == len(A):
                return False
            else:
                return True
            
        count = 0
        for a,b in zip(A,B):
            if a == b:
                continue       
            else:
                if count == 0:
                    da, db = a, b
                    count += 1
                elif count == 1:
                    if da != b or db!= a:
                        return False
                    else:
                        count += 1
                else:
                    return False
        return True
                