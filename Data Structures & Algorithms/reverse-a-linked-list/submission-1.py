# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #We need to check if we have head or not. If we dont have head, we just return None
        if head:
            #Then we need to check if we have next node for the head. If not, then we can just return head
            if head.next:
                #First iteration is special because we need to redirect head.next to the None. We store head and head.next so we can just iterate through them
                current = head
                future = head.next
                current.next = None
                #After pointing our initial node's next value to the None. We can start iteration through linked list. We need to make sure that our future node always has next because we dont want to accidentally point to the nonexistent node. We always store future node's next value in temporary, so we can start switching. 
                while future.next:
                    temporary = future.next
                    future.next = current
                    current = future
                    future = temporary
                #When there is last value in the linked list, we dont have to store temporary because there is no future node's next node. 
                else:
                    future.next = current
                    current = future
                return current
            else: 
                return head
        else:
            return None