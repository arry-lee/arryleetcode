#¼ò»¯Â·¾¶
#2019-08-01 21:14:40

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathlist = path.split('/')
        print(pathlist)
        for x in pathlist:
            if x == '':
                continue
            elif x == '.':
                continue
            elif x == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return '/'+'/'.join(stack)