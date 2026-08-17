# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0 # 자릿수 올림 저장
        answer = ListNode() # 더미 헤드 노드
        current = answer

        while l1 or l2 or flag:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + flag
            flag = 1 if total > 9 else 0
            current.next = ListNode(total % 10)

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return answer.next