"""28. Find the Index of the First Occurrence in a String
Easy
Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    @staticmethod
    def _strStr(haystack: str, needle: str) -> int:
        return haystack.find(needle)

    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        for i in range(len(haystack)):
            if needle == haystack[i: i + len(needle)]:
                return i


test_cases = (
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("hello", "ll", 2),
)
for haystack, needle, answer in test_cases:
    result = Solution.strStr(haystack, needle)
    print(result)
    assert result == answer
