# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
        def tree(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                tree(node.left, node)
                tree(node.right, node)

        graph = defaultdict(list)
        tree(root, None)

        queue = deque([target.val])
        visited = set([target.val])
        current_distance = 0

        while queue:
            if current_distance == k:
                return list(queue)
            level_length = len(queue)
            for _ in range(level_length):
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            current_distance += 1

        return []