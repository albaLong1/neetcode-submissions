class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.store = {}
        self.head = Node()


    def get(self, key: int) -> int:
        if key in self.store:
            #TODO
            if self.capacity == 1:
                return self.store[key]
            
            current = self.head
            while current.next.val != key:
                current = current.next
            temporary = current.next
            current.next = current.next.next
            temporary.next = self.head.next
            self.head.next = temporary
            return self.store[temporary.val]
        else:
            return -1 
        

    def put(self, key: int, value: int) -> None:
        #We check if the key was already inserted, then we can update it
        if key in self.store:
            #TODO
            #We need to find the value first, and then we can update it
            if self.capacity == 1:
                self.store[key] = value
            
            current = self.head
            while current.next.val != key:
                current = current.next
            temporary = current.next
            current.next = current.next.next
            temporary.next = self.head.next
            self.head.next = temporary
            self.store[key] = value
        #If the key hasn't been inserted, then we can add it to the linked list
        else:
            #If the capacity is not reached, we can add another node to the Linked List
            if self.size < self.capacity:
                self.size += 1
                if self.head.next:
                    temporary = self.head.next
                    self.head.next = Node(key)
                    self.head.next.next = temporary
                    self.store[key] = value
                else:
                    self.head.next = Node(key)
                    self.store[key] = value
            #If the capcity is reached, then we need to delete the least recent node in the linked list. Then we need to add the new one.
            else:
                #The deletion of the last Node 
                current = self.head
                while current.next.next:
                    current = current.next
                self.store.pop(current.next.val)
                current.next = None
                #Adding the new node to the non-empty linked list
                if self.head.next:
                    temporary = self.head.next
                    self.head.next = Node(key)
                    self.head.next.next = temporary
                    self.store[key] = value
                #Adding the new node in case if the capacity is only size of 1
                else:
                    self.head.next = Node(key)
                    self.store[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        
