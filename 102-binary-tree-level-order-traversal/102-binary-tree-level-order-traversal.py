# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        queue = [[root, 1]]
        ans = []
        while queue:
            curr, depth = queue.pop(0)
            ans.append([curr.val, depth])
            if curr.left:
                queue.append([curr.left, depth+1])
            if curr.right:
                queue.append([curr.right, depth+1])
        
        final_ans = []
        prev_depth = 1
        temp = []
        for node, depth in ans:
            if depth == prev_depth:
                temp.append(node)
            else:
                final_ans.append(temp)
                temp = [node]
                prev_depth = depth
        final_ans.append(temp)   
        return final_ans
            
        