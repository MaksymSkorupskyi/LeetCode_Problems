"""220. Contains Duplicate III
Hard
https://leetcode.com/problems/contains-duplicate-iii/description/

You are given an integer array nums and two integers indexDiff and valueDiff.
Find a pair of indices (i, j) such that:
1) i != j,
2) abs(i - j) <= indexDiff.
3) abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j),
we cannot satisfy the three conditions, so we return false.

Constraints:
2 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
1 <= indexDiff <= nums.length
0 <= valueDiff <= 10^9
"""


class Solution:
    @staticmethod
    def contains_nearby_almost_duplicate__failed(
        nums: list[int],
        index_diff: int,
        value_diff: int,
    ) -> bool:
        """Memory Limit Exceeded"""
        nums_map = {}
        for i, num in enumerate(nums):
            if num in nums_map and i - nums_map[num] <= index_diff:
                return True

            for n in range(num - value_diff, num + value_diff + 1):
                nums_map[n] = i

        return False

    @staticmethod
    def containsNearbyAlmostDuplicate_v1(
        nums: list[int],
        index_diff: int,
        value_diff: int,
    ) -> bool:
        """Bucketing
        https://leetcode.com/problems/contains-duplicate-iii/solutions/825267/python3-summarizing-contain-duplicates
        -i-ii-iii/
        """
        bucket_map = {}
        for i, num in enumerate(nums):
            bucket_id = num // (value_diff + 1)
            if bucket_id in bucket_map and i - bucket_map[bucket_id][0] <= index_diff:
                return True

            if (
                bucket_id - 1 in bucket_map
                and i - bucket_map[bucket_id - 1][0] <= index_diff
                and abs(num - bucket_map[bucket_id - 1][1]) <= value_diff
            ):
                return True

            if (
                bucket_id + 1 in bucket_map
                and i - bucket_map[bucket_id + 1][0] <= index_diff
                and abs(num - bucket_map[bucket_id + 1][1]) <= value_diff
            ):
                return True

            bucket_map[bucket_id] = (i, num)

        return False

    @staticmethod
    def containsNearbyAlmostDuplicate(
        nums: list[int],
        index_diff: int,
        value_diff: int,
    ) -> bool:
        """Bucketing optimized
        https://leetcode.com/problems/contains-duplicate-iii/solutions/825606/python-3-official-solution-in-python-3-2-methods-explanation/
        """
        bucket_map = {}
        for i, num in enumerate(nums):
            bucket_id = num // (value_diff + 1)

            for bucket_index in (bucket_id, bucket_id - 1, bucket_id + 1):
                if (
                    bucket_index in bucket_map
                    and i - bucket_map[bucket_index][0] <= index_diff
                    and abs(num - bucket_map[bucket_index][1]) <= value_diff
                ):
                    return True

            bucket_map[bucket_id] = (i, num)

        return False


test_cases = (
    ([1, 14, 23, 45, 56, 2, 3], 1, 10, True),
    ([2147483640, 2147483641], 1, 100, True),
    ([-2147483640, -2147483641], 1, 100, True),
    ([-2147483648, 2147483647], 1, 1, False),
    ([2147483647, -1, 2147483647], 1, 2147483647, False),
    ([2147483646, 2147483647], 3, 3, True),
    ([8, 7, 15, 1, 6, 1, 9, 15], 1, 3, True),
    ([1, 2, 3, 1], 3, 0, True),
    ([1, 5, 9, 1, 5, 9], 2, 3, False),
    ([99, 99], 2, 0, True),
    ([1, 2, 3, 1], 3, 0, True),
    ([1, 0, 1, 1], 1, 0, True),
    ([1, 2, 3, 1, 2, 3], 2, 0, False),
    ([7, 2, 8], 2, 1, True),
    ([6, 2, 5, 1, 7, 2, 4], 4, 0, True),
    ([1, 2, 5, 6, 7, 2, 4], 4, 0, True),
    ([1, 2, 1, 1], 1, 0, True),
    ([1, 2, 3, 1], 3, 0, True),
    ([1, 0, 1, 1], 1, 2, True),
    ([1, 2, 2, 3, 4, 5], 3, 0, True),
    ([1, 2, 2, 3, 1], 3, 0, True),
    ([-3, 3, -6], 2, 3, True),
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
)

for case, index_diff, value_diff, expected in test_cases:
    result = Solution.containsNearbyAlmostDuplicate(case, index_diff, value_diff)
    print(result)
    assert result is expected
