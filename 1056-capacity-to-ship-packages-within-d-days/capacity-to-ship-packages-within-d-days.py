class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        leastCapacity = end

        def countDays(capacity):
            days, currentCapacity = 1, capacity
            for weight in weights:
                if currentCapacity - weight < 0:
                    days += 1
                    currentCapacity = capacity
                currentCapacity -= weight
            return days

        while start <= end:
            capacity = (start + end) // 2
            if countDays(capacity) <= days:
                leastCapacity = min(leastCapacity, capacity)
                end = capacity - 1
            else:
                start = capacity + 1

        return leastCapacity

        