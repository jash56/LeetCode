# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        
        elif p and q:
            queue_p, queue_q = [p], [q]
            while queue_p and queue_q:
                temp_p = queue_p.pop(0)
                temp_q = queue_q.pop(0)
                if (temp_p.val != temp_q.val):
                    return False
                else:
                    if temp_p.left and temp_q.left:
                        queue_p.append(temp_p.left)
                        queue_q.append(temp_q.left)
                    elif (not temp_p.left and temp_q.left) or ( temp_p.left and not temp_q.left):
                        return False
                    
                    if temp_p.right and temp_q.right:
                        queue_p.append(temp_p.right)
                        queue_q.append(temp_q.right)
                    elif (not temp_p.right and temp_q.right) or ( temp_p.right and not temp_q.right):
                        return False
            return True
            
        else: return False
        
        
        