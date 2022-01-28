# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post(self, root, ans):
        if not root:
            return None
        self.post(root.left, ans)
        self.post(root.right, ans)
        ans.append(root.val)
        return ans
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.post(root, [])