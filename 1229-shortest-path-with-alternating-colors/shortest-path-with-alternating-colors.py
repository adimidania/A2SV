from collections import deque, defaultdict 

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        answer = []
        
        for u, v in redEdges:
            red_graph[u].append(v)

        for u, v in blueEdges:
            blue_graph[u].append(v)
        

        distances = [[-1, -1] for _ in range(n)]
        distances[0] = [0, 0]  
        
        queue = deque([(0, 0), (0, 1)])
        
        while queue:
            node, color = queue.popleft()
            next_color = 1 - color 
            
            if color == 0:  
                neighbors = blue_graph[node]
            else:  
                neighbors = red_graph[node]
            
            for neighbor in neighbors:
                if distances[neighbor][next_color] == -1:  
                    distances[neighbor][next_color] = distances[node][color] + 1
                    queue.append((neighbor, next_color))
        
        for red_dist, blue_dist in distances:
            if red_dist == -1 and blue_dist == -1:
                answer.append(-1)
            elif red_dist == -1:
                answer.append(blue_dist)
            elif blue_dist == -1:
                answer.append(red_dist)
            else:
                answer.append(min(red_dist, blue_dist))
        
        return answer

