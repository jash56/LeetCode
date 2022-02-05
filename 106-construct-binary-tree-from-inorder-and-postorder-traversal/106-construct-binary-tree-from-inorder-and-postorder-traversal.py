# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.count = 0
    
    def rec(self, left, right, postorder, inorder_map):
        
        if left > right:
            return
        
        node_val = postorder[self.count]
        self.count -= 1
        node = TreeNode(val=node_val)
        node_inorder_idx = inorder_map[node_val]
        node.right = self.rec(node_inorder_idx+1, right, postorder, inorder_map)
        node.left = self.rec(left, node_inorder_idx-1, postorder, inorder_map)
          
        return node
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        left = 0
        right = len(inorder) - 1
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
        self.count = len(inorder)-1  
        
        return self.rec(left, right, postorder, inorder_map)
        