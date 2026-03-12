class Solution {
  ListNode? mergeTwoLists(ListNode? list1, ListNode? list2) {
    ListNode dummy = ListNode(0);
    ListNode current = dummy;

    ListNode? p = list1;
    ListNode? q = list2;

    while (p != null && q != null) {
      if (p.val <= q.val) {
        current.next = ListNode(p.val);
        p = p.next;
      } else {
        current.next = ListNode(q.val);
        q = q.next;
      }

      current = current.next!;
    }

    if (p != null) current.next = p;
    if (q != null) current.next = q;

    return dummy.next;
  }
}