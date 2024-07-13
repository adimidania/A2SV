class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque()
        q.append(["0000", 0])
        visit = set(deadends)

        def children(lock):
            output = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                output.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                output.append(lock[:i] + digit + lock[i+1:])
            return output

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])

        return -1
        