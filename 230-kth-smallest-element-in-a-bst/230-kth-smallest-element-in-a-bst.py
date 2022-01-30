# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, order):
        if not root: return
        self.inorder(root.left, order)
        order.append(root.val)
        self.inorder(root.right, order)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # order = []
        # self.inorder(root, order)
        # return order[k-1]
        
        if not root: return
        
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        
        
        