#∞Ù«Ú±»»¸
#2019-01-07 21:50:22

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1]+stack[-2])
                
            elif op == 'D':
                stack.append(stack[-1]*2)
                
            elif op == 'C':
                stack.pop()
                
            else:
                stack.append(int(op))
                
        return sum(stack)