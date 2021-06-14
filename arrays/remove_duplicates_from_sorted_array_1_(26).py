"""26. Remove Duplicates from Sorted Array [Easy]

Given a sorted array nums,
remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
Given nums = [1,1,2]
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

from typing import List


# Runtime: 72 ms, faster than 97.69% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 16.3 MB, less than 5.58% of Python3 online submissions for Remove Duplicates from Sorted Array.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


# v1: Runtime: 56 ms, beats 100.00 % of python3 submissions!
# https://leetcode.com/submissions/detail/146731879/
# Runtime: 80 ms, faster than 82.31% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 16.3 MB, less than 7.34% of Python3 online submissions for Remove Duplicates from Sorted Array.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)


# Runtime: 80 ms, faster than 82.31% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.9 MB, less than 80.73% of Python3 online submissions for Remove Duplicates from Sorted Array.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] == nums[i]:
                nums.pop(i)
        return len(nums)


# Runtime: 88 ms, faster than 52.60% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.8 MB, less than 94.16% of Python3 online submissions for Remove Duplicates from Sorted
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in reversed(range(1, len(nums))):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)


def main():
    solution = Solution()
    assert solution.removeDuplicates([1, 1, 1]) == 1
    assert solution.removeDuplicates([1, 1, 2]) == 2
    assert solution.removeDuplicates([-1, 0, 0, 0, 0, 3, 3]) == 3


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
