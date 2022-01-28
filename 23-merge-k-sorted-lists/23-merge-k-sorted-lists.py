# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge_two_lists(self, list1, list2):
        
        if not list1 and not list2:
            return
        else:
            temp = ListNode()
            ans = temp
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
                
        return temp.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return
        ans = lists[0]
        for i in range(1, len(lists)):
            ans = self.merge_two_lists(ans, lists[i])
        return ans
        
        
        
        
        