# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root, p, q, found, path):
        
        if not root:
            return
        path.append(root)
        
        if root.val == p.val:           
            found.append(list(path))     
        elif root.val == q.val:
            found.append(list(path))        
        if len(found) == 2:
            return    
        
        self.traverse(root.left, p, q, found, path)
        self.traverse(root.right, p, q, found, path)
        path.pop()      
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found = []
        path = []
        self.traverse(root, p, q, found, path)
        
        idx = 0
        n = min(len(found[0]), len(found[1]))
        
        while idx < n:
            if found[0][idx].val == found[1][idx].val:
                idx += 1  
            else:
                break
        return found[0][idx-1]
        
        