class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = []
        for char, freq in count.items():
            heapq.heappush(max_heap, (-freq, char))
        
        prev_char = ''
        prev_freq = 0
        result = []
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_char = char
            prev_freq = freq + 1

        rearranged = ''.join(result)
        return rearranged if len(rearranged) == len(s) else ""
