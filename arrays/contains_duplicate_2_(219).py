"""219. Contains Duplicate II [Easy]

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""

from typing import List


# Runtime: 624 ms, faster than 5.28% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 32.5 MB, less than 5.41% of Python3 online submissions for Contains Duplicate II.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num not in index_map:
                index_map[num] = [i]
            else:
                # duplicate detected
                if i - index_map[num][-1] <= k:
                    return True
                index_map[num].append(i)

        return False


# Runtime: 596 ms, faster than 5.28% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 28.4 MB, less than 5.41% of Python3 online submissions for Contains Duplicate II.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                # duplicates detected
                return True
            index_map[num] = i

        return False


solution = Solution()
for test_case, k, expected in (
        ([1, 2, 3, 1], 3, True,),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
):
    print(test_case, solution.containsNearbyDuplicate(test_case, k), expected)
    assert solution.containsNearbyDuplicate(test_case, k) == expected
