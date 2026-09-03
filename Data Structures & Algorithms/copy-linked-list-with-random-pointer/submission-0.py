"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #When creating dictionary, we have to state if the value is zero, then we have null value
        oldToCOopy = {None : None}
        cur = head
        #Mapping old nodes to new copied nodes
        while cur:
            node = Node(cur.val)
            oldToCOopy[cur] = node
            cur = cur.next
        
        cur = head
        #Connecting all new copied nodes using dictionary 
        while cur:
            node = oldToCOopy[cur]
            node.next = oldToCOopy[cur.next]
            node.random = oldToCOopy[cur.random]
            cur = cur.next

        return oldToCOopy[head]
        