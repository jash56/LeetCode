# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder_idx = 0
        
    def rec(self, subtree_inorder_start, subtree_inorder_end, preorder, inorder_index_map):
        
        if subtree_inorder_start > subtree_inorder_end:
            return
        
        root = TreeNode(val=preorder[self.preorder_idx])
        self.preorder_idx += 1
        root.left = self.rec(subtree_inorder_start, inorder_index_map[root.val]-1, preorder, inorder_index_map)
        root.right = self.rec(inorder_index_map[root.val]+1, subtree_inorder_end, preorder, inorder_index_map)
        
        return root
        
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        count = 0
        inorder_index_map = {} 
        for i in inorder:            
            inorder_index_map[i] = count
            count += 1
                  
        return self.rec(0, len(inorder)-1, preorder, inorder_index_map)
            