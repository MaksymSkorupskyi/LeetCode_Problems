"""220. Contains Duplicate III [Medium]

Given an integer array nums and two integers k and t,
return True if there are two distinct indices i and j in the array such that
abs(nums[i] - nums[j]) <= t
and
abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

Constraints:
0 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^4
0 <= t <= 2^31 - 1
"""
import collections
from typing import List


# Time Limit Exceeded
class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums) - 1):
            k_nums = sorted(nums[i: i + 1 + k])
            for j in range(len(k_nums) - 1):
                if k_nums[j + 1] - k_nums[j] <= t:
                    return True

        return False


# Time Limit Exceeded
class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(nums[i] - nums[j]) <= t:
                    return True

        return False


class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # sort `nums` array preserving nums indices
        elements = sorted(zip(range(len(nums)), nums), key=lambda x: x[1])

        collections.OrderedDict().popitem(False)

        print(elements)

        for i in range(len(nums) - 1):
            print(i, elements[i], elements[i-1])
            print(abs(elements[i][0] - elements[i - 1][0]))
            print(abs(elements[i][1] - elements[i - 1][1]))

            # for j in range(k):
            if abs(elements[i][1] - elements[i - 1][1]) <= t and abs(elements[i][0] - elements[i - 1][0]) <= k:
                return True

        return False


solution = Solution()
for test_case, k, t, expected in (
        ([7, 2, 8], 2, 1, True),
        ([6, 2, 5, 1, 7, 2, 4], 4, 0, True),
        ([1, 2, 5, 6, 7, 2, 4], 4, 0, True),
        ([2147483646, 2147483647], 3, 3, True,),
        ([1, 2, 1, 1], 1, 0, True,),
        ([1, 2, 3, 1], 3, 0, True,),
        ([1, 0, 1, 1], 1, 2, True),
        ([1, 2, 2, 3, 4, 5], 3, 0, True,),
        ([1, 2, 2, 3, 1], 3, 0, True,),
        ([-3, 3, -6], 2, 3, True,),
        ([1, 14, 23, 45, 56, 2, 3], 1, 10, True,),
        ([8, 7, 15, 1, 6, 1, 9, 15], 1, 3, True,),
        ([2147483640, 2147483641], 1, 100, True,),
        ([-2147483640, -2147483641], 1, 100, True,),
        ([1, 2, 1, 1], 1, 0, True),
        ([1, 5, 9, 1, 5, 9], 2, 3, False),
        ([], 0, 0, False),
        ([0], 0, 0, False),
        ([1], 1, 1, False),
        ([1, 2], 0, 1, False),
        ([2, 4], 1, 1, False),
        ([4, 2], 2, 1, False),
        ([-3, 3], 2, 4, False),
        ([1, 3, 1], 1, 1, False),
        ([1, 3, 1], 2, 1, True),
        ([-2147483648, 2147483647], 1, 1, False),
        ([2147483647, -1, 2147483647], 1, 2147483647, False),
):
    print(test_case, solution.containsNearbyAlmostDuplicate(test_case, k, t), expected)
    assert solution.containsNearbyAlmostDuplicate(test_case, k, t) == expected
