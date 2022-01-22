# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(next=head)
        ptr = head
        length = 1
        while ptr.next:
            length += 1
            ptr = ptr.next

#         if count == 1: return None
#         elif count == 2 and n == 2: return head.next
#         elif count == 2 and n == 1:
#             head.next = None
#             return head
        
        n = length - n + 1
        ptr = dummy
        i = 0
        while i < n-1:
            i += 1
            ptr = ptr.next
            
        ptr.next = ptr.next.next
        
        return dummy.next
        
        