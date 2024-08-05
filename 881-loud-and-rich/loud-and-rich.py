class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        if len(richer) == 0:
            return list(range(len(quiet)))
        
        answer = list(range(len(quiet)))
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        
        for a, b in richer:
            graph[a].append(b)
            indegrees[b] += 1
            
        queue = deque([i for i in range(len(quiet)) if indegrees[i] == 0])
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if quiet[answer[current]] < quiet[answer[neighbor]]:
                    answer[neighbor] = answer[current]
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return answer