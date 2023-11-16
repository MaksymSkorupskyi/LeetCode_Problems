"""217. Contains Duplicate
Easy
11.1K
1.2K
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    @staticmethod
    def contains_duplicate_v1(nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True

            nums_set.add(num)

        return False


test_cases = (
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([99, 99], True),
    ([1, 2, 3, 1], True),
    ([1, 0, 1, 1], True),
    ([1, 2, 3, 1, 2, 3], True),
)

for case, answer in test_cases:
    result = Solution.containsDuplicate(case)
    print(result)
    assert result is answer
