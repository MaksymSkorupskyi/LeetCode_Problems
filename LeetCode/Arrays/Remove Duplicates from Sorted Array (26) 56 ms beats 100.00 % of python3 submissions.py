"""26. Remove Duplicates from Sorted Array
Given nums = [1,1,2]
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

# v1: Runtime: 56 ms, beats 100.00 % of python3 submissions!
# https://leetcode.com/submissions/detail/146731879/
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)


# v2: Runtime: 64 ms, beats 96.40 % of python3 submissions.
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)


# v3: Runtime: 76 ms, beats 68.31 % of python3 submissions.
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in reversed(range(1, len(nums))):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)


def main():
    a = Solution()
    print(a.removeDuplicates([1,1,1]))
    print(a.removeDuplicates([1,1,2]))
    print(a.removeDuplicates([-1, 0, 0, 0, 0, 3, 3]))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')