# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def ser(self, root, s):
        if not root: 
            s.append('x')
            return
        s.append(str(root.val))
        self.ser(root.left, s)
        self.ser(root.right, s)
        return s

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        s = []
        self.ser(root, s)
        return ','.join(s)
        
    def des(self, data):
        
        if data:
            if data[0] == 'x':
                data.pop(0)
                return
            root = TreeNode(data.pop(0))
            root.left = self.des(data)
            root.right = self.des(data)
            return root
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = data.split(',')
        return self.des(data)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans