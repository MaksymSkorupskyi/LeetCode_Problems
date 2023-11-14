"""242. Valid Anagram
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters?
How would you adapt your solution to such a case?
"""
from string import ascii_lowercase


class Solution:
    @staticmethod
    def is_anagram_v1(s: str, t: str) -> bool:
        """nlog(n) + mlog(m) sorted strings"""
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    @staticmethod
    def is_anagram_v2(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # "abcdefghijklmnopqrstuvwxyz"
        for char in ascii_lowercase:
            if s.count(char) != t.count(char):
                return False

        return True

    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        """O(n)"""
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        for x, y in zip(s, t):
            s_map[x] = s_map.get(x, 0) + 1
            t_map[y] = t_map.get(y, 0) + 1

        return s_map == t_map


test_cases = (
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("aa", "a", False),
    ("aacc", "ccace", False),
)
for x, y, answer in test_cases:
    result = Solution.isAnagram(x, y)
    print(result)
    assert result == answer
