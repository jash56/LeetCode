# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def ser(self, root, ans):    
        if root is None:
            ans += 'x,'                            
        else:
            ans += str(root.val) + ','           
            ans = self.ser(root.left, ans)
            ans = self.ser(root.right, ans)
    # print(','.join(ans))
        return ans
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.ser(root, '')
    
    def des(self, data):
        if data[0] == 'x':
            data.pop(0)
            return None
        
        root = TreeNode(data.pop(0))
        root.left = self.des(data)
        root.right = self.des(data)
        return root
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        return self.des(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))