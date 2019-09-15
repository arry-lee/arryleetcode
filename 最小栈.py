#×îÐ¡Õ»
#2019-08-13 05:45:10

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x,x))
        else:
            _min = min(self.stack[-1][1],x)
            self.stack.append((x,_min))
            
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            raise IndexError('Empty stack')

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            raise IndexError('Empty stack')

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()