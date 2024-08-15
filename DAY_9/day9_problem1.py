class MinStack(object):
    def __init__(self):
        self.a=[]
        
    def push(self, val):
        self.a.append(val)

    def pop(self):
        if self.a:
            self.a.pop()

    def top(self):
        return self.a[-1]

    def getMin(self):
        return min(self.a)

# Example usage:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
