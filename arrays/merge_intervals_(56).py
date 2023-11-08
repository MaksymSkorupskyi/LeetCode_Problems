"""56. Merge Intervals [Medium]

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List


# v1 use sort()
# Runtime: 84 ms, faster than 77.54% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16.2 MB, less than 10.22% of Python3 online submissions for Merge Intervals.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = []
        merged_interval = [intervals[0][0], intervals[0][1]]
        for i, interval in enumerate(intervals, start=1):
            if interval[0] <= merged_interval[1]:
                merged_interval[1] = max(merged_interval[1], interval[1])
            else:
                merged_intervals.append(merged_interval)
                merged_interval = interval
        merged_intervals.append(merged_interval)

        return merged_intervals


# Runtime: 88 ms, faster than 54.47% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16 MB, less than 96.84% of Python3 online submissions for Merge Intervals.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = []
        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                # if the list of merged intervals is empty or if the current
                # interval does not overlap with the previous, simply append it.
                merged_intervals.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals


def main():
    solution = Solution()

    print(solution.merge([[15, 18], [1, 3], [8, 10], [2, 6]]))
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solution.merge([[1, 4], [4, 5]]))
    print(solution.merge([[1, 4], [0, 4]]))
    print(solution.merge([[1, 4], [2, 3]]))

    assert solution.merge([[15, 18], [1, 3], [8, 10], [2, 6]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert solution.merge([[1, 4], [2, 3]]) == [[1, 4]]


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
