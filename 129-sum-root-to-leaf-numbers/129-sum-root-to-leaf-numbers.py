# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, path_list, current_path):
        if not root: return
        current_path.append(root.val)
        if not root.left and not root.right:
            path_list.append(list(current_path))
        self.dfs(root.left, path_list, current_path)
        self.dfs(root.right, path_list, current_path)
        current_path.pop()    
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path_list = []
        current_path = []
        self.dfs(root, path_list, current_path)
        ans = 0
        for path in path_list:
            temp = ''
            for i in path:
                temp += str(i)
            ans += int(temp)
        return ans
        
    
    