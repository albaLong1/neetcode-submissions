from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        temp = deque()
        if len(self.queue) != 0:
            while len(self.queue) > 1:
                value = self.queue.popleft()
                temp.append(value)
            answer = self.queue.popleft()
            self.queue = temp
            return answer
        

    def top(self) -> int:
        temp = deque()
        if len(self.queue) != 0:
            while len(self.queue) > 1:
                value = self.queue.popleft()
                temp.append(value)
            answer = self.queue[0]
            temp.append(answer)
            self.queue = temp
            return answer
        

    def empty(self) -> bool:
        return (len(self.queue) == 0)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()