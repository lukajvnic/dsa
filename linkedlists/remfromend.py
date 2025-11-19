# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {str(self.next)}"

class Solution:
    def removeNthFromEnd(self, head, n: int):
        cur = head
        target = None
        length = 0

        while cur is not None:
            if length >= n:
                if target is None:
                    target = head
                else:
                    target = target.next

            length += 1
            cur = cur.next

        if length == n:
            return head.next
        else:
            target.next = target.next.next
        return head


sol = Solution()
test = ListNode(1, 
print(sol.removeNthFromEnd(test, 1))
