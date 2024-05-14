class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals_sorted = sorted((start, i) for i, (start, _) in enumerate(intervals))
        output = []
        for start, end in intervals:
            low, high = 0, len(intervals_sorted) - 1
            answer = -1
            while low <= high:
                mid = (low + high) // 2
                if intervals_sorted[mid][0] >= end:
                    answer = intervals_sorted[mid][1]
                    high = mid - 1
                else:
                    low = mid + 1
            output.append(answer)
        return output