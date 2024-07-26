class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        count = Counter(s)
        heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(heap)
        prev = None
        while heap or prev:
            if prev and not heap:
                return ""
            
            cnt, char = heapq.heappop(heap)
            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
                
            if cnt:
                prev = [cnt, char]
            
        return res
