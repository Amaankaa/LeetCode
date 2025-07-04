# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = set()
        i = 0
        while head:
            if head in cnt:
                return head
                
            cnt.add(head)
            head = head.next

        return head