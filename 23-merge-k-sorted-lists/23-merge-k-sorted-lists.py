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
        
        ans = lists
        while len(ans) != 1:
            n = len(ans)
            merged = []
            for i in range(0, n-1, 2):
                lst1 = ans.pop(0)
                lst2 = ans.pop(0)
                merged.append(self.merge_two_lists(lst1, lst2))
            ans = ans + merged
        return ans[0]
        
        
        
        
        