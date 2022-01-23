# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_match(self, p, q):
        if p and q:
            if p.val == q.val:
                return True
            else: 
                return False
        elif not p and not q:
            return True
        
        return False
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        
        elif p and q:
            queue = [(p, q)]
            while queue:
                p_curr, q_curr = queue.pop(0)
                if not self.is_match(p_curr, q_curr):
                    return False
                if p_curr:
                    queue.append((p_curr.left, q_curr.left))
                    queue.append((p_curr.right, q_curr.right))
                    
            return True
            
        else:
            return False
        
        
        