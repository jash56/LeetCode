# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return head
        pt1, pt2 = head, head.next
        pt1.next = None
        while pt2:
            temp = pt2.next
            pt2.next = pt1
            pt1 = pt2
            pt2 = temp
        return pt1
            
            
            
            