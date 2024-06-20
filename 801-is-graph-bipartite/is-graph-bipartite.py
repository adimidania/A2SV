class Solution:
    def isBipartite(self, graph):
        colors = [0] * len(graph)
        def dfs(graph, colors, index, color):
            if colors[index] != 0:
                return colors[index] == color

            colors[index] = color

            for neighbor in graph[index]:
                if not dfs(graph, colors, neighbor, -color):
                    return False

            return True

        for i in range(len(graph)):
            if colors[i] == 0:
                if not dfs(graph, colors, i, 1):
                    return False

        return True

