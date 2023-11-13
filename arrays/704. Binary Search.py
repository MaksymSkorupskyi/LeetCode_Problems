"""704. Binary Search
https://leetcode.com/problems/binary-search/
Easy
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
 If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """Algorithm
        Initialize the boundaries of the search space as left = 0 and right = nums.size - 1.
        If there are elements in the range [left, right],
        we find the middle index mid = (left + right) / 2
        and compare the middle value nums[mid] with target:
            1. If nums[mid] = target, return mid.
            2. If nums[mid] < target, let left = mid + 1 and repeat step 2.
            3. If nums[mid] > target, let right = mid - 1 and repeat step 2.
        We finish the loop without finding target, return -1.
        """
        # Set the left and right boundaries
        left = 0
        right = len(nums) - 1

        # Under this condition
        while left <= right:
            # Get the middle index and the middle value.
            mid = (left + right) // 2

            if nums[mid] == target:
                # Case 1, return the middle index.
                return mid

            if nums[mid] < target:
                # Case 2, discard the smaller half.
                left = mid + 1
            else:
                # Case 3, discard the larger half.
                right = mid - 1

        # If we finish the search without finding target, return -1.
        return -1


test_cases = (
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
)
for nums, target, answer in test_cases:
    s = Solution()
    result = s.search(nums, target)
    print(result)
    assert result == answer
