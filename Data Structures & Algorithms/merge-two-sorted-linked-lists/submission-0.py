# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        result = None




        if list1.val <= list2.val:
            print("adding list1", list1.val)

            result = list1
            list1 = list1.next
        else:
            print("adding list2", list2.val)
            result = list2
            list2 = list2.next
        curr = result
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                print("adding list1", list1.val)
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            elif list2.val <= list1.val:
                print("adding list2", list2.val)
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            
            
        while list1 is not None:
            print("adding list1", list1.val)
            curr.next = list1
            list1 = list1.next
            curr = curr.next

        while list2 is not None:
            print("adding list2", list2.val)
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        return result
