class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        max_freq = max(freq.values())

        count_max = 0
        for f in freq.values():
            if f == max_freq:
                count_max += 1

        intervals = (max_freq - 1) * (n + 1) + count_max

        return max(len(tasks), intervals)
