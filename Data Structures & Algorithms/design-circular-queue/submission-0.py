class Node:

    def __init__(self, val: int, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.tail = None
        self.head = None
        
        

    def enQueue(self, value: int) -> bool:
        #We need to check if the list is full
        if self.isFull():
            return False
        #Then we need to check if it is empty.
        #If it is empty, we need to assign both tail and head to the newest node. Also increment the size by 1. 
        if self.isEmpty():
            node = Node(value)
            self.tail = node
            self.head = node
            self.size += 1
            return True
        else:
            #If the stack is not empty we need to create new node which node.next = head, and head.prev = node. And then we can head = head.prev so the pointer will be moved to the newly created node.
            node = Node(value)
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev
            self.size += 1
            return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            node = self.tail.prev
            if node:
                node.next = None
                self.tail = self.tail.prev
                self.size -= 1
                if self.isEmpty():
                    self.head = None
                return True
            else:
                self.size -= 1 
                self.head = None
                self.tail = None
                return True
        

        

    def Front(self) -> int:
        if self.tail:
            return self.tail.val
        else:
            return -1
        

    def Rear(self) -> int:
        if self.head:
            return self.head.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False
        



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()