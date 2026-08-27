class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if value not in self.mins:
            if not self.mins:
                self.mins.append(value)
            else:
                if self.mins[-1] > value:
                    self.mins.append(value)

    def pop(self) -> None:
        value = self.stack.pop()
        if value not in self.stack and value in self.mins:
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