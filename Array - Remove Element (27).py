"""27. Remove Element
Given an array and a value, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
"""

# v1: Runtime: 40 ms, beats 95.18 % of python3 submissions.

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


# v2: Runtime: 44 ms, beats 86.14 % of python3 submissions.

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [x for x in nums if x != val]
        return len(nums)


def main():
    a = Solution()
    print(a.removeElement(nums = [3,2,2,3], val = 3))
    print(a.removeElement([1,1,1], 1))
    print(a.removeElement([1,1,2], 1))
    print(a.removeElement([-1, 0, 0, 0, 0, 3, 3], 0))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')