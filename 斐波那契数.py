#ì³²¨ÄÇÆõÊı
#2019-07-25 22:56:00

class Solution:
    def fib(self, N: int) -> int:
        
        a,b=0,1
        while N>0:
            a,b = b,a+b
            N -= 1
        return a