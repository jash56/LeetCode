# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, low, high):
        
        if not root: return False
        
        if low <= root.val <= high:
            return root
        elif low > root.val:
            return self.dfs(root.right, low, high)
        else:
            return self.dfs(root.left, low, high)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val > q.val:
            p, q = q, p
        
        return self.dfs(root, p.val, q.val)
        
    