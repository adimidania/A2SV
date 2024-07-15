class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        output = [[float('inf') for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    output[i][j] = 0
                    queue.append((i, j))
                    visited.add((i, j))  

        while queue:
            i, j = queue.popleft()
            s = output[i][j]
            for (d1, d2) in directions:
                i1, j1 = i + d1, j + d2
                if 0 <= i1 < len(mat) and 0 <= j1 < len(mat[0]) and (i1, j1) not in visited:
                    if output[i1][j1] > s + 1:
                        output[i1][j1] = s + 1
                        queue.append((i1, j1))
                        visited.add((i1, j1)) 
                    
        return output
