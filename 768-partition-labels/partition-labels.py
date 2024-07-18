class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        last_occurences = {num: i for i, num in enumerate(s)}
        i = j = k = 0
        for i, num in enumerate(s):
            k = max(k , last_occurences[num])
            if k == i:
                output.append(i - j + 1)
                j = i + 1
        return output

        