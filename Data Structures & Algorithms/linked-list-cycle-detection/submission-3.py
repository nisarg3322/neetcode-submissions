# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        if head == head.next:
            return True
       

        slow = head
        fast = head.next.next

        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            
            slow = slow.next
            fast = fast.next.next
        
        return False