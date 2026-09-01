# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        addOne = False
        while l1 and l2:
            if addOne:
                value = l1.val + l2.val + 1
                addOne = False
            else:
                value = l1.val + l2.val
            integer = value % 10
            tail.next = ListNode(integer)
            addOne = True if value >= 10 else False
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            if addOne:
                value = l1.val + 1
                addOne = False
            else:
                value = l1.val
            integer = value % 10
            tail.next = ListNode(integer)
            addOne = True if value >= 10 else False
            tail = tail.next
            l1 = l1.next
        
        while l2:
            if addOne:
                value = l2.val + 1
                addOne = False
            else:
                value = l2.val
            integer = value % 10
            tail.next = ListNode(integer)
            addOne = True if value >= 10 else False
            tail = tail.next
            l2 = l2.next
        
        if addOne:
            tail.next = ListNode(1)
        

        return dummy.next

        