"""692. Top K Frequent Words
Medium
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation:
"the", "is", "sunny" and "day" are the four most frequent words,
with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:
1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
"""
from collections import Counter
from heapq import nsmallest


class Solution:
    @staticmethod
    def top_k_frequent_v1(words: list[str], k: int) -> list[str]:
        # Count the frequency of each word
        counter = Counter(words)

        # Create buckets to store words based on their frequency
        buckets = [[] for _ in range(len(counter) + 1)]

        # Assign each word to its respective bucket
        for word, freq in counter.items():
            buckets[freq].append(word)

        # Flatten the buckets and sort the words in descending order
        flattened_buckets = [
            w for bucket in buckets for w in sorted(bucket, reverse=True)
        ]

        # Return the top k frequent words
        return flattened_buckets[::-1][:k]

    @staticmethod
    def top_k_frequent_v2(words: list[str], k: int) -> list[str]:
        # Count the frequency of each word
        counter = Counter(words)

        # Create buckets to store words based on their frequency
        buckets = [[] for _ in range(len(counter) + 1)]

        # Assign each word to its respective bucket
        for word, freq in counter.items():
            buckets[freq].append(word)

        # Flatten the buckets and sort the words in ascending order
        flattened_buckets = [w for bucket in buckets[::-1] for w in sorted(bucket)]

        # Return the top k frequent words
        return flattened_buckets[:k]

    @staticmethod
    def top_k_frequent_v3(words: list[str], k: int) -> list[str]:
        # Count the frequency of each word
        counter = Counter(words)

        # Create buckets to store words based on their frequency
        buckets = [[] for _ in range(len(counter) + 1)]

        # Assign each word to its respective bucket
        for word, freq in counter.items():
            buckets[freq].append(word)

        # Create a result list to store the top k frequent words
        result = []

        # Iterate through the buckets in reverse order
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]

            # If the bucket is not empty, sort the words and add them to the result list
            if bucket:
                result.extend(sorted(bucket))

        # Return the top k frequent words
        return result[:k]

    @staticmethod
    def top_k_frequent_v4(words: list[str], k: int) -> list[str]:
        # Count the frequency of each word
        counter = Counter(words)

        # Sort the words based on their frequency and alphabetical order
        sorted_words = sorted(counter, key=lambda x: (-counter[x], x))

        # Return the top k frequent words
        return sorted_words[:k]

    @staticmethod
    def topKFrequent(words: list[str], k: int) -> list[str]:
        """The idea is to leverage the heap data structure,
        comparing elements by frequency (in decreasing order)
        and then by lexicographical order (increasing).
        """
        counter = Counter(words)
        return nsmallest(k, counter.keys(), key=lambda x: (-counter[x], x))


test_cases = (
    (
        ["i", "love", "leetcode", "i", "love", "coding"],
        3,
        ["i", "love", "coding"],
    ),
    (
        ["i", "love", "leetcode", "i", "love", "coding"],
        2,
        ["i", "love"],
    ),
    (
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
        4,
        ["the", "is", "sunny", "day"],
    ),
)

for case, k, expected in test_cases:
    result = Solution.topKFrequent(case, k)
    print(result)
    assert result == expected
