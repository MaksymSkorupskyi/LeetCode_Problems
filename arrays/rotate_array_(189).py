"""189. Rotate Array [Medium]

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List


# 1. brute force
# Runtime: 3116 ms, faster than 8.13% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.4 MB, less than 83.78% of Python3 online submissions for Rotate Array.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Do not return anything, modify nums in-place instead."""
        for _ in range(k):
            n = nums.pop(-1)
            nums.insert(0, n)


# 2. O(1)
# Runtime: 192 ms, faster than 99.78% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.3 MB, less than 96.60% of Python3 online submissions for Rotate Array.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Do not return anything, modify nums in-place instead."""
        steps = k % len(nums)  # handle case when k >= len(nums)
        nums[:] = nums[-steps:] + nums[:-steps]


def main():
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums=nums, k=3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    solution.rotate(nums=nums, k=2)
    assert nums == [3, 99, -1, -100]

    nums = [1,2]
    solution.rotate(nums=nums, k=3)
    assert nums == [2, 1]


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
