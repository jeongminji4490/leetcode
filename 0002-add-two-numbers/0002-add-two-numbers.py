# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        result = dummy

        flag = 0

        while curr1 is not None or curr2 is not None or flag:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            val = val1 + val2 + flag
            flag = val // 10

            result.next = ListNode(val % 10)
            result = result.next
            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next

        return dummy.next
            