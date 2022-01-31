class Solution:
    def make_graph(self, prerequisites):
        graph = {}
        for edge in prerequisites:
            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
        return graph
    
    def is_cycle(self, graph, start, visited, checked):
        if start not in graph:
            return False        
        if start in checked:
            return False
        
        if start in visited:
            return True   
        visited.add(start)
        for neighbor in graph[start]:   
            if self.is_cycle(graph, neighbor, visited, checked):
                return True
        visited.remove(start)
        checked.add(start)
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        graph = self.make_graph(prerequisites)
        checked = set()
        for course in graph:
            visited = set()
            if self.is_cycle(graph, course, visited, checked):
                return False
        return True
        
            