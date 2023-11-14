"""290. Word Pattern
Easy
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match,
such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
from itertools import zip_longest


class Solution:
    @staticmethod
    def word_pattern_v1(pattern: str, s: str) -> bool:
        """Using itertools.zip_longest()"""
        s = s.split()

        return len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern, s)))

    @staticmethod
    def word_pattern_v2(pattern: str, s: str) -> bool:
        """Using zip()"""
        s = s.split()
        # Initial validation of pattern and s lengths
        if len(pattern) != len(s):
            return False

        return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))

    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        words = s.split()
        # Initial validation of pattern and s lengths
        if len(pattern) != len(words):
            return False

        pattern_map = {}
        unique_words = set()
        # Iterate over pattern and words
        for p, word in zip(pattern, words):
            # Case 1: word is already mapped in pattern_map to another p
            if p not in pattern_map and word in unique_words:
                return False

            # Case 2: word mismatch with already mapped in pattern_map
            if p in pattern_map and pattern_map[p] != word:
                return False

            # Case 3: map p with word
            pattern_map[p] = word
            unique_words.add(word)

        return True


test_cases = (
    ("abba", "dog dog dog dog", False),
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
)
for x, y, answer in test_cases:
    result = Solution.wordPattern(x, y)
    print(result)
    assert result == answer
