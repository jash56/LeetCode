# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, low, high):        
        if not root: return True      
        if low >= root.val or root.val >= high:
            return False       
        # if not root.left and not root.right:
        #     return True 
        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, high)
            
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:   
        return self.dfs(root, float('-inf'), float('inf'))
        