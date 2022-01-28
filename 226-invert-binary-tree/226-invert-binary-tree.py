# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def invert(self, root):
        if not root:
            return None
        root.left = self.invert(root.left)
        root.right = self.invert(root.right)
        root.left, root.right = root.right, root.left
        return root
        
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # if not root: return None
        # queue = [root]
        # while queue:
        #     curr = queue.pop(0)
        #     if curr.left:
        #         queue.append(curr.left)
        #     if curr.right:
        #         queue.append(curr.right)
        #     curr.left, curr.right = curr.right, curr.left
        # return root
        return self.invert(root)