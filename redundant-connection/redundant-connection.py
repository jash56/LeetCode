class Solution:
    
    # function to find parent/representative/root of given node
    def find(self, parent_list, node):
        parent = parent_list[node]
        while parent != parent_list[parent]:
            parent = parent_list[parent]
        return parent
            
    # function to combine 2 subsets based on the rank of their roots        
    def union(self, parent_list, u_representative, v_representative):
        # u has higher rank than v
        if parent_list[u_representative] < parent_list[v_representative]:
            #parent_list[u_representative] += parent_list[v_representative]
            parent_list[v_representative] = u_representative
        else:
            #parent_list[v_representative] += parent_list[u_representative]
            parent_list[u_representative] = v_representative
        return parent_list
        
    # function to find the edge of cycle removing which will make a tree
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent_list = [i for i in range((len(edges) + 1))]
        rank = [1] * len(parent_list)
        for u, v in edges:  
            u_root = self.find(parent_list, u)
            v_root = self.find(parent_list, v)
            if u_root == v_root:
                return [u, v]
            else:
                self.union(parent_list, u_root, v_root)
                
            
        