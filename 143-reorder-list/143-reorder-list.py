# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """    
        # get end of list
        end = head
        while end.next:
            end = end.next
        
        #get middle element of list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        
        #flip the list from middle to end
        prev, curr = mid, mid.next
        mid.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 2 ptr one from start and one from end
        start = head
        while end.next:
            temp = start.next
            start.next = end
            start = temp
            
            temp = end.next
            end.next = start
            end = temp
        
        return head
            
            
            
        
