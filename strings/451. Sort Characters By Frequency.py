"""451. Sort Characters By Frequency
Medium
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.


Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Constraints:
1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.
"""
from collections import Counter


class Solution:
    @staticmethod
    def frequency_sort_v1(s: str) -> str:
        # Count the frequency of each character
        counter = Counter(s)

        # Sort the characters based on their frequency in descending order
        sorted_chars = sorted(counter, key=counter.get, reverse=True)

        # Create a new string by repeating each character the number of times it appears in the original string
        return "".join([c * counter[c] for c in sorted_chars])

    @staticmethod
    def frequency_sort_v2(s: str) -> str:
        # Count the frequency of each character
        counter = Counter(s)

        # Sort the characters based on their frequency in descending order
        sorted_chars = sorted(counter.elements(), key=counter.get, reverse=True)

        # Create a new string by repeating each character the number of times it appears in the original string
        return "".join([c for c in sorted_chars])

    @staticmethod
    def frequency_sort_v3(s: str) -> str:
        # Count the frequency of each character
        counter = Counter(s)

        # Get the characters and their frequencies in descending order
        sorted_chars = counter.most_common()

        # Create a new string by repeating each character
        # the number of times it appears in the original string
        return "".join([c * freq for c, freq in sorted_chars])

    @staticmethod
    def frequency_sort_v4(string: str) -> str:
        """Bucket sort by char frequency"""
        # Create a frequency map to store the count of each character
        freq_map = {}
        for char in string:
            freq_map[char] = freq_map.get(char, 0) + 1

        # Create buckets to store characters based on their frequency
        buckets = [[] for _ in range(len(string) + 1)]
        for char, freq in freq_map.items():
            buckets[freq].append(char * freq)

        # Join the characters in reverse order from the buckets
        return "".join([s for bucket in buckets for s in bucket][::-1])

    @staticmethod
    def frequencySort(string: str) -> str:
        """Bucket sort by char frequency"""
        # Create a frequency map to store the count of each character
        freq_map = Counter(string)

        # Create buckets to store characters based on their frequency
        buckets = [[] for _ in range(len(string) + 1)]
        for char, freq in freq_map.items():
            buckets[freq].append(char * freq)

        # Join the characters in reverse order from the buckets
        result = ""
        for i in range(len(buckets) - 1, -1, -1):
            result += "".join([s for s in buckets[i]])

        return result


test_cases = (
    ("tree", {"eert", "eetr"}),
    ("Aabb", {"bbAa", "bbaA"}),
    ("cccaaa", {"aaaccc", "cccaaa"}),
)

for case, expected in test_cases:
    result = Solution.frequencySort(case)
    print(result)
    assert result in expected
