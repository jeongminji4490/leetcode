# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        curr1 = list1
        curr2 = list2
        dummy = ListNode(0)
        result = dummy

        while curr1 or curr2:
            if curr2 is None or (curr1 and curr1.val <= curr2.val):
                result.next = ListNode(curr1.val)
                result = result.next
                curr1 = curr1.next
            else:
                result.next = ListNode(curr2.val)
                result = result.next
                curr2 = curr2.next

        return dummy.next


