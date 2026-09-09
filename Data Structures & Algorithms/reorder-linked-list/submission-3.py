# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        The confusion is created because we need to modify the linked list. We need to modify in the way that L_1 -> L_n -> L_2 and etc until we put in order all nodes from the list. The Linked list doesn't repeat the same node. 
        The first thought is to count how many nodes do we have in the linked list. Based on that we can find the middle of the linked list and cut it in half which first half will be longer by 1 node or it will be same amount of nodes as the right half. Next we can reverse the second half. After reversing we can start combining them together through taversing them and while both have nodes. Then we need to check we have an extra node in the right half and add it to the linked list in the end.
        """
        #Creating dummy as a reference
        dummy = ListNode(0)

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        if length <= 2:
            return
        
        secondHalfNodesAmount = length // 2
        firstHalfNodesAmount = length - secondHalfNodesAmount
        tail = head
        for _ in range(firstHalfNodesAmount):
            tail = tail.next
        
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        #Linked list is constructed in the way that intial nodes will be in the odd positon and reversed nodes are in the even position
        even = reverse(tail)
        odd = head
        ans = dummy

        for _ in range(secondHalfNodesAmount):
            ans.next = odd
            odd = odd.next
            ans = ans.next
            
            ans.next = even
            even = even.next
            ans = ans.next

            
            
        
        if firstHalfNodesAmount - secondHalfNodesAmount != 0:
            ans.next = odd
            ans = ans.next
        
        ans.next = None 

        head = dummy.next