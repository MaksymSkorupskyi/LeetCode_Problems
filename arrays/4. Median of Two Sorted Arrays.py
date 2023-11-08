"""4. Median of Two Sorted Arrays
Hard
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        length = len(merged_array)
        if length % 2 == 0:
            return (merged_array[length // 2 - 1] + merged_array[length // 2]) / 2

        return merged_array[length // 2]


test_cases = (
    ([1, 3], [2], 2),
    ([1, 2], [3, 4], 2.5),
    ([1, 1], [1, 2], 1),
)
for nums1, nums2, answer in test_cases:
    print(nums1, nums2, Solution.findMedianSortedArrays(nums1, nums2))
    assert Solution.findMedianSortedArrays(nums1, nums2) == answer
