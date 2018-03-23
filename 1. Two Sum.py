"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Учитывая массив целых чисел, возвращайте индексы двух чисел так, чтобы они добавлялись к определенной цели.
Вы можете предположить, что каждый вход будет иметь ровно одно решение,
и вы не можете использовать один и тот же элемент дважды.

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
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     num_dict = {}
#     for i in range(len(nums)):
#        complement = target - nums[i]
#        if complement in num_dict:
#          return [num_dict[complement], i]
#        else:
#          num_dict[nums[i]] = i

# def twoSum(nums, target):
#     if len(nums) <= 1:
#         return False
#     buff_dict = {}
#     for i in range(len(nums)):
#         if nums[i] in buff_dict:
#             return [buff_dict[nums[i]], i]
#         else:
#             buff_dict[target - nums[i]] = i

# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if len(nums) <= 1:
#             return False
#         for x in range(len(nums)-1):
#             for y in range(x + 1, len(nums)):
#                 if nums[y] == target - nums[x]:
# #                if nums[x] + nums[y] == target:
#                     return [x, y]



"""
# working code:

for x in range(len(nums)-1):
#    print(x, nums[x])
    for y in range(x+1, len(nums)):
#        print(y, nums[y])
        if nums[x] + nums[y] == target:
           print([x, y])


# expertiments

# for idx,val in enumerate(nums):
#    print(idx, nums[idx])

for y in nums:
        print(len(nums))
        print(y)
        print(x+y)
        input()
        if x + y == target:
            print(nums.index(x), nums.index(x))


for idx in range(len(nums)):
    val = nums[idx]
    print(idx)
    print(val)
    print(nums)
"""