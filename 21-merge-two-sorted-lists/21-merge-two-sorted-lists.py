# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None        
        else:
            dummy = ListNode()
            ans = dummy
            while list1 and list2: 
                if list1.val <= list2.val:
                    ans.next = list1
                    ans = ans.next
                    list1 = list1.next
                else:
                    ans.next = list2
                    ans = ans.next
                    list2 = list2.next
        
        if list1:
            ans.next = list1
        elif list2:
            ans.next = list2
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        if not list1 and not list2:
            return
        elif not list1:
            return list2
        elif not list2:
            return list1
            
        if list1.val < list2.val:
            ans = list1
            list1 = list1.next
        else:
            ans = list2
            list2 = list2.next
        temp = ans
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
        
        return ans
            
        