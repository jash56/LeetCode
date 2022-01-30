# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#         if root:
#             depth = 0
#             queue = [(1, root)]
#             while queue:
#                 curr_depth, curr = queue.pop(0)
#                 depth = max(depth, curr_depth)
#                 if curr.left:
#                     queue.append((curr_depth+1, curr.left))
#                 if curr.right:
#                     queue.append((curr_depth+1, curr.right))
#         else: return 0
#         return depth
        