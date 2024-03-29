"""169. Majority Element
Easy
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    @staticmethod
    def majorityElement_v1(nums: List[int]) -> int:
        """With count()"""
        majority = len(nums) / 2
        nums_map = {}
        for n in nums:
            if n not in nums_map:
                nums_map[n] = nums.count(n)
            if nums_map[n] > majority:
                return n

    @staticmethod
    def majorityElement_v2(nums: List[int]) -> int:
        """Without count()"""
        majority = len(nums) / 2
        nums_map = {}
        for n in nums:
            if n not in nums_map:
                nums_map[n] = 1
            else:
                nums_map[n] += 1
            if nums_map[n] > majority:
                return n

    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        """Without count()"""
        majority = len(nums) / 2
        nums_map = {}
        for n in nums:
            nums_map[n] = nums_map.get(n, 0) + 1
            if nums_map[n] > majority:
                return n


test_cases = (
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
)
for nums, answer in test_cases:
    result = Solution.majorityElement(nums)
    print(result)
    assert result == answer

