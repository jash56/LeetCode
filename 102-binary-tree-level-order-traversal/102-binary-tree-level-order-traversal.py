# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = [root]
        ans = []
        level = 0
        
        while queue:
            
            level_length = len(queue)
            curr = [queue.pop(0) for i in range(level_length)]
            ans.append([node.val for node in curr])
            for node in curr:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans
            
        