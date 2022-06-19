"""1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
nums = [2, 7, 11, 15]
target = 9

Because
nums[0] + nums[1] = 2 + 7 = 9
return [0, 1]
"""
from typing import List, Tuple


# 2022 Memoization O(n)
# Runtime: 64 ms, faster than 92.66% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 49.76% of Python3 online submissions for Two Sum.
class Solution:
    @classmethod
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        memo = {}
        for i, num in enumerate(nums):
            if target - num in memo:
                return memo[target - num], i
            memo[num] = i


print(Solution.twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution.twoSum(nums=[3, 2, 4], target=6))
print(Solution.twoSum(nums=[3, 3], target=6))


# 2022 brute force O(n^2)
# Runtime: 6091 ms, faster than 11.41% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 95.11% of Python3 online submissions for Two Sum.
class Solution:
    @classmethod
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


print(Solution.twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution.twoSum(nums=[3, 2, 4], target=6))
print(Solution.twoSum(nums=[3, 3], target=6))


# 2017 memoization
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    buff_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in buff_dict:
            return buff_dict[complement], i
        else:
            buff_dict[nums[i]] = i


a = twoSum([2, 7, 11, 15], 9)
print(a)
"""
# 2017 solution
class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        for x in range(len(self.nums)-1):
            for y in range(x + 1, len(self.nums)):
                if self.nums[x] + self.nums[y] == self.target:
                    return [x, y]

result = Solution([3, 2, 4], 6)

print(result.twoSum())

# nums = [2, 7, 11, 15]
# target = 9

"""
