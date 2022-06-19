"""217. Contains Duplicate [Easy]

Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


# Runtime: 112 ms, faster than 91.96% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 20.4 MB, less than 41.81% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


solution = Solution()
for test_case, expected in (
        ([1, 2, 3, 1], True,),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
):
    print(test_case, solution.containsDuplicate(test_case), expected)
    assert solution.containsDuplicate(test_case) == expected
