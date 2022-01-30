# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rec(self, root, path, ans):
        
        if not root:
            return ans
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if not root: return []
        stack = [(root, [root.val])]
        ans = []
        while stack:
            curr, curr_path = stack.pop(-1)
            if not curr.left and not curr.right and sum(curr_path) == targetSum:
                ans.append(curr_path)          
            
            if curr.right:     
                stack.append((curr.right, curr_path + [curr.right.val]))
                
            if curr.left: 
                stack.append((curr.left, curr_path + [curr.left.val]))
        return ans