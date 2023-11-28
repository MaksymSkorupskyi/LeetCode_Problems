"""41. First Missing Positive
Hard

Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    @staticmethod
    def first_missing_positive_v1(nums: list[int]) -> int:
        """Space O(n)"""
        nums_set = set(nums)
        for i in range(1, 2 ** 31):
            if i not in nums_set:
                return i

    @staticmethod
    def firstMissingPositive(nums: list[int]) -> int:
        """Space O(n)"""
        nums_set = {n for n in nums if n > 0}
        for i in range(1, 2 ** 31):
            if i not in nums_set:
                return i


test_cases = (
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
)

for nums, expected in test_cases:
    result = Solution.firstMissingPositive(nums)
    print(result)
    assert result is expected
