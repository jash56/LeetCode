# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def rec(root):
            if not root: return 0
            nonlocal max_sum
            left = max(rec(root.left), 0)
            right = max(rec(root.right), 0)

            new_start = root.val + left + right
            max_sum = max(max_sum, new_start)
            return max(root.val+left, root.val+right)
        rec(root)
        return max_sum