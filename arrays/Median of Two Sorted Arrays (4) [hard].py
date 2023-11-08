"""
4. Median of Two Sorted Arrays [hard]
https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""


# with .median() static method:
# Runtime: 96 ms, beats 98.42% of python3 submissions.
class Solution:
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    @staticmethod
    def median(x):
        if len(x) % 2:
            return x[len(x) // 2]
        else:
            return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2

    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        return self.median(nums)


# straight solution:
# class Solution:
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: float
#     """
#     def findMedianSortedArrays(self, nums1, nums2):
#         nums = nums1 + nums2
#         nums.sort()
#         if len(nums) % 2:
#             return nums[len(nums) // 2]
#         return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2


def main():
    a = Solution()
    print(a.findMedianSortedArrays([1, 3], [2]))
    print(a.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
