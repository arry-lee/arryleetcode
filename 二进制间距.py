#二进制间距
#2019-01-08 11:01:39

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        A = [i for i in range(32) if (N>>i) & 1]
        if len(A) < 2:
            return 0
        return max(A[i+1] - A[i] for i in range(len(A) - 1))