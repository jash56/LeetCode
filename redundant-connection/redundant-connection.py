class Solution:
    
    def create_vertex_list(self, edges):
        vertex_list = []
        for u, v in edges:
            if u not in vertex_list:
                vertex_list.append(u)
            if v not in vertex_list:
                vertex_list.append(v)
        return vertex_list
    
    def find(self, parent_list, node):
        node = node - 1
        parent = parent_list[node]
        while parent != -1:
            node = parent
            parent = parent_list[node]      
        return node
            
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent_list = [-1] * len(self.create_vertex_list(edges))
        
        for u, v in edges:
            
            u_representative = self.find(parent_list, u)
            v_representative = self.find(parent_list, v)
            
            if u_representative == v_representative:
                return [u, v]
            else:
                parent_list[u_representative] = v_representative
                
            
        