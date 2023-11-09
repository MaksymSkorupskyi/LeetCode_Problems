"""347. Top K Frequent Elements
Medium
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List


class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        element_freq = {}  # Dict[element , freq]
        for n in nums:
            if n not in element_freq:
                element_freq[n] = nums.count(n)
        freq = {}
        for key, value in element_freq.items():
            if value not in freq:
                freq[value] = [key]
            else:
                freq[value].append(key)
        result = []
        for key in sorted(freq.keys(), reverse=True)[:k]:
            result.extend(freq[key])

        print(element_freq)
        print(freq)
        print(sorted(freq.keys(), reverse=True)[:k])

        return result


test_cases = (
    # ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([5, -4, 5, 5, -4, 3], 2, [-4, 5]),
    ([19, 10], 2, [10, 19]),
    ([3, 0, 1, 0], 1, [0]),
    ([1], 1, [1]),
)

for case, k, answer in test_cases:
    result = Solution.topKFrequent(case, k)
    print(result)
    assert set(result) == set(answer)
