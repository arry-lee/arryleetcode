#比较含退格的字符串
#2019-07-25 22:47:25

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 栈
        stack_s = []
        for s in S:
            if s != '#':
                stack_s.append(s)
            else:
                if stack_s:
                    stack_s.pop()
                else:
                    pass
        
        stack_t = []
        for s in T:
            if s != '#':
                stack_t.append(s)
            else:
                if stack_t:
                    stack_t.pop()
                else:
                    pass
        print(stack_s,stack_t)
        return stack_s == stack_t
        