# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # curr1 = list1
        # curr2 = list2
        dummy = ListNode(0)
        result = dummy

        while list1 or list2:
            if list2 is None or (list1 and list1.val <= list2.val):
                result.next = ListNode(list1.val)
                result = result.next
                list1 = list1.next
            else:
                result.next = ListNode(list2.val)
                result = result.next
                list2 = list2.next

        return dummy.next


