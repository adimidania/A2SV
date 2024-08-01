class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = defaultdict(set)
        graph = defaultdict(list)
        
        for from_node, to_node in edges:
            graph[to_node].append(from_node)
        
        def dfs(node):
            if node in ancestors:
                return ancestors[node]
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(dfs(parent))
            return ancestors[node]
        
        order = [[] for _ in range(n)]
        for i in range(n):
            order[i] = sorted(dfs(i))
        
        return order