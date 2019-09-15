#¸´Êý³Ë·¨
#2019-01-08 10:51:34

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, ai = a.rstrip('i').split('+')
        ca = complex(int(ar), int(ai))
        br, bi = b.rstrip('i').split('+')
        cb = complex(int(br), int(bi))

        c = ca*cb
        return "%d+%di" %(c.real,c.imag)