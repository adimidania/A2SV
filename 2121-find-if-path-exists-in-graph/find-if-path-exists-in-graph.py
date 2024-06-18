class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(vertex, visited):
            if vertex == destination: 
                visited.add(vertex)
                return 
            
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    dfs(node, visited)

        dfs(source, visited)
        if destination in visited:
            return True
        else:
            return False
            
        