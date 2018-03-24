"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
nums = [2, 7, 11, 15]
target = 9

Because
nums[0] + nums[1] = 2 + 7 = 9
return [0, 1]
"""

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
