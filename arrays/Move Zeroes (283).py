"""283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# v1: Runtime: 44 ms, beats 100.00 % of python3 submissions.
# https://leetcode.com/submissions/detail/146757708/


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzeroes = [x for x in nums if x != 0]
        if nonzeroes and len(nonzeroes) < len(nums):
            nums[: len(nonzeroes)] = nonzeroes
            nums[len(nonzeroes) :] = [0] * (len(nums) - len(nonzeroes))


# v2: beautiful but not so fast. Runtime: 116 ms, beats 27.97 % of python3 submissions.


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums.count(0) < len(nums):
            for i in range(nums.count(0)):
                nums.remove(0)
                nums.append(0)

        print(nums)


def main():
    a = Solution()
    print(a.moveZeroes(nums=[0, 1, 0, 3, 12]))
    print(a.moveZeroes(nums=[3, 2, 2, 3]))
    print(a.moveZeroes([1, 1, 1]))
    print(a.moveZeroes([1, 1, 2]))
    print(a.moveZeroes([-1, 0, 0, 0, 0, 3, 3]))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
