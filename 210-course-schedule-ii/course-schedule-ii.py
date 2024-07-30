class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque([])
        order = []
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.appendleft(course)
        
        while queue:
            node = queue.pop()
            order.append(node)
            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.appendleft(course)

        if len(order) != numCourses:
            return []
        return order