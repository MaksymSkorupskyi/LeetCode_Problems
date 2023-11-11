"""26. Remove Duplicates from Sorted Array
Easy
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements
in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums
being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates_v1(nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)


test_cases = (
    ([1, 1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
)
for nums, answer in test_cases:
    result = Solution.removeDuplicates(nums)
    print(result)
    assert result == answer
