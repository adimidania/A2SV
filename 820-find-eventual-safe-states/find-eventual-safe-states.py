class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [len(adj) for adj in graph]  
        reverse_graph = [[] for _ in range(n)]  
        
        for i in range(n):
            for neighbor in graph[i]:
                reverse_graph[neighbor].append(i)
        
        queue = deque()
        print(reverse_graph)
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
        
        output = []
        while queue:
            node = queue.popleft()
            output.append(node)
            for neighbor in reverse_graph[node]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted(output)