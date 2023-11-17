"""215. Kth Largest Element in an Array
Medium
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

import heapq


class Solution:
    @staticmethod
    def find_kth_largest_v1(nums: list[int], k: int) -> int:
        """Using sorted()"""
        return sorted(nums)[-k]

    @staticmethod
    def find_kth_largest_v2(nums: list[int], k: int) -> int:
        """Using heapq.nlargest()"""
        return heapq.nlargest(k, nums)[-1]

    @staticmethod
    def find_kth_largest_v3(nums: list[int], k: int) -> int:
        """heapq.heappop() + heapq.heappush()"""
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

    @staticmethod
    def find_kth_largest_v4(nums: list[int], k: int) -> int:
        """heapq.heappop() + heapq.heappush() optimized"""
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        return min_heap[0]

    @staticmethod
    def find_kth_largest_v5(nums: list[int], k: int) -> int:
        """heapq.heappushpop()"""
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

    @staticmethod
    def findKthLargest(nums: list[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value


test_cases = (
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ([1, 2, 3, 4, 5, 6], 2, 5),
    ([1, 2, 2, 3, 3, 4, 5, 5, 6], 4, 4),
)

for nums, k, expected in test_cases:
    result = Solution.findKthLargest(nums, k)
    print(result)
    assert result == expected
