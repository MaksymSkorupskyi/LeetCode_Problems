"""448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n


Follow up:
Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
"""
# Runtime: 346 ms, faster than 97.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 24.4 MB, less than 37.61% of Python3 online submissions for Find All Numbers Disappeared in an Array.
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_unique = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in nums_unique]


# Runtime: 567 ms, faster than 40.95% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 26.4 MB, less than 11.93% of Python3 online submissions for Find All Numbers Disappeared in an Array.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)) - set(nums)
