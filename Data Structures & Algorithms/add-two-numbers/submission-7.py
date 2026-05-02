# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        head = curr
        while l1 is not None or l2 is not None:
            if curr.next is None:
                curr.next = ListNode(0)
            curr = curr.next
            if l1 is not None and l2 is not None:
                total = l1.val + l2.val
            elif l1 is not None and l2 is None:
                
                total = l1.val +curr.val
                curr.val = 0
                print("in l1" , total)
            else:
                total = l2.val + curr.val
                curr.val =0
                print("in l2", total)
            print(total)
            if total <= 9:
                curr.val += total
                
            elif total > 9 :
                l,r = total // 10, total % 10
                print("l,r: ", l,r)
                curr.val += r
                curr.next = ListNode(l)

            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:

                l2 = l2.next

            
        return head.next