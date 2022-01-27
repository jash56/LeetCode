# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: return False
        queue = [(root, root.val)]
        
        while queue:
            curr, curr_sum = queue.pop(-1)  
            if not curr.left and not curr.right and curr_sum == targetSum:
                return True
            if curr.left:
                queue.append((curr.left, curr_sum + curr.left.val)) 
            if curr.right:
                queue.append((curr.right, curr_sum + curr.right.val))
            
        return False
                