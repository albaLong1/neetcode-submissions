# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        tail.next = head
        counter = 0
        while tail.next:
            counter += 1
            tail = tail.next

        #When to break is number = total - n
        number = counter - n
        
        ans = dummy
        recorder = 0
        while ans:
            if recorder == number:
                if ans.next.next:
                    ans.next = ans.next.next
                    break
                else:
                    ans.next = None
                    break
            recorder += 1
            ans = ans.next
        
        return dummy.next
        