# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # 1. Reach the node right before the reversal begins
        before_sublist = dummy
        for _ in range(left - 1):
            before_sublist = before_sublist.next

        # 2. Standard reversal inside the [left, right] window
        # curr will start as the first node in the window (the future tail of this segment)
        curr = before_sublist.next
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Stitch the anchors back together
        # before_sublist.next is the original start of the window (now its tail)
        # curr is now the first untouched node after the window (right + 1)
        # prev is now the new head of the reversed window (right)
        before_sublist.next.next = curr
        before_sublist.next = prev

        return dummy.next
        