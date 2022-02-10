class Solution:
    
    def get_indegree_graph(self, edges, num):
        graph = defaultdict(list)
        indegree = [0] * num
        for edge in edges:
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        return graph, indegree
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph, indegree = self.get_indegree_graph(prerequisites, numCourses)
        allowed = []
        ans = []
        for idx, degree in enumerate(indegree):
            if degree == 0:
                allowed.append(idx)
        
        while allowed: 
            curr = allowed.pop()
            ans.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    allowed.append(neighbor)           
            graph.pop(curr)
        
        for i in indegree:
            if i != 0:
                return []
        return ans