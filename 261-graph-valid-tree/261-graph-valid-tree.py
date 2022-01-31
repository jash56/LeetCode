class Solution:
    
    def cycle(self, graph, root, visited):
        # if not root: return False
        print(root)
        if root in visited:
            print('caught', root)
            return True
        visited.add(root)
        for neighbor in graph[root]:
            graph[neighbor].remove(root)
            if self.cycle(graph, neighbor, visited):
                return True
        return False
               
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        if self.cycle(graph, 0, visited):
            return False
        for vertex in range(n):
            if vertex not in visited:
                return False             
        return True
            
        
            
        