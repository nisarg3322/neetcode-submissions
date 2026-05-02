# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        if head is None or (head.next is None and n == 1):
            return None

        first = second = head
        prev = second

        # move first pointer n times
        for i in range(0,n-1):
            first = first.next

        print("first:", first.val)

        while first is not None and first.next is not None:
            first = first.next
            prev = second
            second = second.next
        print("prev", prev.val)
        print("second",second.val)
        if second is head and n > 1:
            return head.next
        prev.next = second.next
        
        return head;
