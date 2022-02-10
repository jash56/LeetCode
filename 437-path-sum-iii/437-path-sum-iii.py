# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
          
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0    
        path_prefix = collections.defaultdict(int)
        
        def rec(root, curr_sum):            
            if not root: return 0
            nonlocal ans
            curr_sum = curr_sum + root.val
            
            if curr_sum == targetSum:
                ans += 1        
            ans += path_prefix[curr_sum - targetSum]
            path_prefix[curr_sum] += 1
            rec(root.left, curr_sum)
            rec(root.right, curr_sum)
            path_prefix[curr_sum] -= 1            

        rec(root, 0)
        return ans