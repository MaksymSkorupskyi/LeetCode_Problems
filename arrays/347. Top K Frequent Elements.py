"""347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
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
from collections import Counter


class Solution:
    @staticmethod
    def top_k_frequent_v1(nums: List[int], k: int) -> List[int]:
        """v1: using count() function"""
        # O(1) time
        if k >= len(nums):
            return nums

        element_freq = {}  # Dict[element, freq]
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
        for key in sorted(freq.keys(), reverse=True):
            result.extend(freq[key])

        return result[:k]

    @staticmethod
    def top_k_frequent_v2(nums: List[int], k: int) -> List[int]:
        """v2: no count() function"""
        # O(1) time
        if k >= len(nums):
            return nums

        element_freq = {}  # Dict[element, freq]
        for n in nums:
            element_freq[n] = element_freq.get(n, 0) + 1
        freq = {}
        for key, value in element_freq.items():
            freq[value] = freq.get(value, []) + [key]
        result = []
        for key in sorted(freq.keys(), reverse=True):
            result.extend(freq[key])

        return result[:k]

    @staticmethod
    def top_k_frequent_v3(nums: List[int], k: int) -> List[int]:
        """v3: bucket sort"""
        # O(1) time
        if k >= len(nums):
            return nums

        element_freq = {}  # Dict[element, freq]
        for n in nums:
            element_freq[n] = element_freq.get(n, 0) + 1

        buckets = [[] for _ in range(max(element_freq.values()) + 1)]
        for n, freq in element_freq.items():
            buckets[freq].append(n)
        flat_list = [n for bucket in buckets for n in bucket]

        return flat_list[-k:]

    @staticmethod
    def top_k_frequent_v4(nums: List[int], k: int) -> List[int]:
        """v4: sort frequency map by frequency"""
        # O(1) time
        if k >= len(nums):
            return nums

        element_freq = {}  # Dict[element, freq]
        for n in nums:
            element_freq[n] = element_freq.get(n, 0) + 1

        return sorted(element_freq, key=element_freq.get)[-k:]

    @staticmethod
    def top_k_frequent_v5(nums: List[int], k: int) -> List[int]:
        """v5: Counter + most_common(k) O(Nlogk)"""
        # O(1) time
        if k >= len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        counter = Counter(nums)

        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return [n for n, _ in counter.most_common(k)]

    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        """v5: Counter + heapq.nlargest(k) O(Nlogk)"""
        # O(1) time
        if k >= len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        counter = Counter(nums)

        # Lazy import to speedup Python startup time
        from heapq import nlargest
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return nlargest(k, counter.keys(), key=counter.get)



test_cases = (
    ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
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
