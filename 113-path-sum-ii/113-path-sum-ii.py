# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rec(self, root, path, ans, targetSum):
        
        if not root: return 
        path.append(root.val)
        if not root.left and not root.right and root.val == targetSum:
            ans.append(list(path))
        else:          
            self.rec(root.left, path, ans, targetSum-root.val)
            self.rec(root.right, path, ans, targetSum-root.val)
        
        path.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        
        self.rec(root, [], ans, targetSum)  
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not root: return []
        # stack = [(root, [root.val])]
        # ans = []
        # while stack:
        #     curr, curr_path = stack.pop(-1)
        #     if not curr.left and not curr.right and sum(curr_path) == targetSum:
        #         ans.append(curr_path)          
        #     if curr.left: 
        #         stack.append((curr.left, curr_path + [curr.left.val]))
        #     if curr.right:     
        #         stack.append((curr.right, curr_path + [curr.right.val]))
        # return ans