# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    
    def is_same(self, root1, root2):
        
        if not root1 and not root2: return True
        
        if root1 and root2:
            
            if root1.val == root2.val:
                return self.is_same(root1.left, root2.left) and self.is_same(root1.right, root2.right)
            
        else: return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = collections.deque()
        stack.append(root)
        while stack:
            curr = stack.pop()
            if self.is_same(curr, subRoot):
                return True
            elif curr:
                stack.append(curr.right)
                stack.append(curr.left)   
        return False