import collections
class Solution:
    
    def make_graph(self, edges):
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])   
        return graph
            
    def bfs(self, graph, start):    
        queue = [start]
        visited = []
        while queue:
            current = queue.pop(0)
            visited.append(current)
            for neigh in graph[current]:
                if neigh not in visited:
                    queue.append(neigh)
        return visited
            
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.make_graph(edges)
        component_count = 0
        visited = set()
        for vertex in range(n):
            if vertex not in visited:
                visited.update(self.bfs(graph, vertex))
                component_count += 1
        return component_count
        