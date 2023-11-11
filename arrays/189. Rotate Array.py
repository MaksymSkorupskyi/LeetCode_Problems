"""189. Rotate Array
Medium
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

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
Try to come up with as many solutions as you can.
There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List


class Solution:
    @staticmethod
    def rotate_v1(nums: List[int], k: int) -> list[int]:
        """Do not return anything, modify nums in-place instead.
        O(n)
        """
        length = len(nums)
        if k > length:
            k = k % length
        nums[:] = nums[length - k :] + nums[: length - k]

        return nums

    @staticmethod
    def rotate_v2(nums: List[int], k: int) -> list[int]:
        """Do not return anything, modify nums in-place instead.
        O(n)
        """
        k = k % len(nums)  # handle case when k >= len(nums)
        if not k:
            return nums

        nums[:] = nums[-k:] + nums[:-k]

        return nums

    @staticmethod
    def rotate_v3(nums: List[int], k: int) -> list[int]:
        """Do not return anything, modify nums in-place instead.
        O(k * n)
        """
        k = k % len(nums)  # handle case when k >= len(nums)
        if not k:
            return nums

        for _ in range(k):
            nums.insert(0, nums.pop(-1))

        return nums

    @staticmethod
    def rotate_v4(nums: List[int], k: int) -> list[int]:
        """Do not return anything, modify nums in-place instead.
        O(k * n)
        """
        length = len(nums)
        k = k % length  # handle case when k >= len(nums)
        if not k:
            return nums

        # Reverse the whole array
        nums.reverse()

        # Reverse the first k elements
        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

        # Reverse the remaining elements
        for i in range(k, (length + k) // 2):
            nums[i], nums[length - 1 - i + k] = nums[length - 1 - i + k], nums[i]

        return nums

    @staticmethod
    def rotate(nums: List[int], k: int) -> list[int]:
        """Do not return anything, modify nums in-place instead.
        O(k * n)
        """
        length = len(nums)
        k = k % length  # handle case when k >= len(nums)
        if not k:
            return nums

        # Reverse the whole array
        nums.reverse()

        # Reverse the first k elements
        nums[:k] = nums[:k][::-1]

        # Reverse the remaining elements
        nums[k:] = nums[k:][::-1]

        return nums


test_cases = (
    ([1, 2], 5, [2, 1]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
)
for nums, k, answer in test_cases:
    result = Solution.rotate(nums, k)
    print(result)
    assert result == answer
