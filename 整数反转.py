#整数反转
#2019-08-13 00:24:59

class Solution:
    def reverse(self, x: int) -> int:
        op = x>0
        x = abs(x)
        x = str(x)
        x = list(x)
        x.reverse()
        x = ''.join(x)
        x = int(x)
        x = x if op else -x
        if -pow(2,31)<=x<pow(2,31):
            return x
        else:
            return 0