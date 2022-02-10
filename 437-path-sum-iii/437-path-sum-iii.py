# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rec(self, root, target_sum, path_prefix, curr_sum):
        
        if not root: return 0
        
        curr_sum = curr_sum + root.val
        
        ans = 0
        if curr_sum == target_sum:
            ans += 1        
        ans += path_prefix[curr_sum - target_sum]
        path_prefix[curr_sum] += 1
        # print(ans, curr_sum, target_sum, path_prefix)   
        left = self.rec(root.left, target_sum, path_prefix, curr_sum)
        right = self.rec(root.right, target_sum, path_prefix, curr_sum)
        
        path_prefix[curr_sum] -= 1
        
        return ans + left + right
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        curr_sum = 0  
        path_prefix = collections.defaultdict(int)
        
        return self.rec(root, targetSum, path_prefix, curr_sum)