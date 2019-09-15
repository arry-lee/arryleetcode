#颠倒二进制位
#2019-08-13 06:59:43

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res=('{:032b}'.format(n))[::-1]
        return int(res,2)