"""219. Contains Duplicate II
Easy
https://leetcode.com/problems/contains-duplicate-ii/
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that
nums[i] == nums[j] and
abs(i - j) <= k.


Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import List


class Solution:
    @staticmethod
    def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        nums_map = {}
        for i, num in enumerate(nums):
            if num in nums_map and i - nums_map[num] <= k:
                return True

            nums_map[num] = i

        return False


test_cases = (
    ([99, 99], 2, True),
    ([1, 2, 3, 1], 3, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False),
)

for case, k, answer in test_cases:
    result = Solution.containsNearbyDuplicate(case, k)
    print(result)
    assert result is answer
