# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(root, depth):
            
            if not root:
                return depth - 1
            
            left_depth = dfs(root.left, depth + 1)
            right_depth = dfs(root.right, depth + 1)
            
            nonlocal diameter
            diameter = max(diameter, (left_depth - depth) + (right_depth - depth))
                
            return max(left_depth, right_depth)
            
        depth = 0
        dfs(root, depth)
        return diameter