#±¨Êý
#2019-08-13 01:50:43

class Solution:
    def countAndSay(self, n: int) -> str:
        # self.countAndSay(n-1)
        if n == 1: return '1'
        if n == 2: return '11'
        s = self.countAndSay(n-1)
        
        stack = []
        i = 1
        len_n = len(s)
        c = 1
        
        while i < len_n:
            if s[i]==s[i-1]:
                c += 1
            else:
                stack.append(str(c))
                stack.append(s[i-1])
                c = 1
            i += 1
        else:
            stack.append(str(c))
            stack.append(s[i-1])
        # print(stack)
        return ''.join(stack)
        
        
            