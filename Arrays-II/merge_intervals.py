class Solution:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"[{self.start} - {self.end}]"


def mergeIntervals(intervals: list[Solution]) -> list[Solution]:
    intervals.sort(key=lambda x: (x.start, x.end))
    ans = []
    ans.append(intervals[0])
    n = len(intervals)
    for i in range(1, n):
        if intervals[i].start <= ans[-1].end:
            ans[-1].end = max(ans[-1].end, intervals[i].end)
        else:
            ans.append(intervals[i])
    return ans


arr = [
    Solution(1, 3),
    Solution(2, 6),
    Solution(8, 10),
    Solution(2, 4),
    Solution(15, 18)
]

print(mergeIntervals(arr))
