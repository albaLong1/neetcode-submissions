class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        val = min(value, self.mins[-1] if self.mins else value)
        self.mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()