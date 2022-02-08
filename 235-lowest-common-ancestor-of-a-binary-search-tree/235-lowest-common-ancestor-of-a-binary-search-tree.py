# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def find(self, root, low, high):
        
        if not root:
            return
        if low.val <= root.val <= high.val:
            return root  
        
        if root.val < low.val:
            return self.find(root.right, low, high)
        elif root.val > high.val:
            return self.find(root.left, low, high)
        
        return 
                    
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p        
        return self.find(root, p, q)