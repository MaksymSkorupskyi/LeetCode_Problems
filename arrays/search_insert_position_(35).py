"""35. Search Insert Position [Easy]

Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

from typing import List


# O(log n)
# Runtime: 36 ms, faster than 99.61% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15.1 MB, less than 52.73% of Python3 online submissions for Search Insert Position.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # checking middle position
            idx = (left + right) // 2
            num = nums[idx]
            if num == target:
                return idx
            # halving the range
            if num < target:
                left = idx + 1
            else:
                right = idx - 1
        # target not  found
        return left


# O(n)
# Runtime: 40 ms, faster than 97.81% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15 MB, less than 52.73% of Python3 online submissions for Search Insert Position.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n >= target:
                return i
        return len(nums)


# O(n)
# Runtime: 44 ms, faster than 91.18% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15 MB, less than 52.73% of Python3 online submissions for Search Insert Position.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            for i, n in enumerate(nums):
                if n >= target:
                    return i
        return len(nums)


def main():
    solution = Solution()

    assert solution.searchInsert(nums=[1, 3, 5, 6, 7], target=1) == 0
    assert solution.searchInsert(nums=[1, 3, 5, 6, 7], target=3) == 1
    assert solution.searchInsert(nums=[1, 3, 5, 6, 7], target=5) == 2
    assert solution.searchInsert(nums=[1, 3, 5, 6, 7], target=6) == 3
    assert solution.searchInsert(nums=[1, 3, 5, 6, 7], target=7) == 4
    assert solution.searchInsert(nums=[1, 3, 5, 6], target=5) == 2
    assert solution.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
    assert solution.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
    assert solution.searchInsert(nums=[1, 3, 5, 6], target=0) == 0
    assert solution.searchInsert(nums=[1], target=0) == 0


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
