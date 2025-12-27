# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def ll_to_num(self, lst, depth):  # depth starts at 1
        if lst is None:
            return 0
        return lst.val * depth + self.ll_to_num(lst.next, depth * 10)

    def num_to_ll(self, num):
        if num == 0:
            return None
        return ListNode(num % 10, self.num_to_ll(num // 10))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.ll_to_num(l1, 1)
        n2 = self.ll_to_num(l2, 1)
        s = n1 + n2
        if s == 0:
            return ListNode(0, None)
        return self.num_to_ll(s)