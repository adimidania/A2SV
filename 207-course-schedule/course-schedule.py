from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()
        def dfs(course):
            if course in visited:
                return False

            if graph[course] == []:
                return True

            visited.add(course)
            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

