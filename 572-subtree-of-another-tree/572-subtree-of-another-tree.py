# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSame(self, root1, root2):    
        
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1 and root2:
            if root1.val == root2.val:
                return self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot: return True
        
        elif root and subRoot:
            
            if root.val == subRoot.val and self.isSame(root, subRoot):  
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        else: return False
                