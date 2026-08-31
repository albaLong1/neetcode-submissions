# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                current = head
                future = head.next
                current.next = None
                while future.next:
                    temporary = future.next
                    future.next = current
                    current = future
                    future = temporary
                else:
                    future.next = current
                    current = future
                return current
            else: 
                return head
        else:
            return None
        