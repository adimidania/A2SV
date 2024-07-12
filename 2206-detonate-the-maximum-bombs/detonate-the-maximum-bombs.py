class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+ 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2)**2 + (y1 - y2)**2)

                if d <= r1:
                    adj_list[i].append(j)

                if d <= r2:
                    adj_list[j].append(i)

        def dfs(i, visit):
            if i in visit:
                return 0
            visit.add(i)
            for nei in adj_list[i]:
                dfs(nei, visit)
            return len(visit)

        output = 0
        for i in range(len(bombs)):
            output = max(output, dfs(i, set()))
        return output

        