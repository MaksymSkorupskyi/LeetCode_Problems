"""205. Isomorphic Strings
Easy
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character
while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


# https://leetcode.com/problems/isomorphic-strings/solutions/2701544/1-line-python-4-line-java-8-line-c-beats98
# /?envType=study-plan-v2&envId=top-interview-150
# The given solution uses the set() function and zip() function to check for isomorphism in a compact way.
# Here is how the code works:
# 1) The set(s) returns the set of unique characters in string s,
# and set(t) returns the set of unique characters in string t.
# 2) The zip(s,t) function returns an iterator of tuples
# where each tuple contains corresponding characters from s and t.
# For example, if s="egg" and t="add", then zip(s,t) returns ('e', 'a'), ('g', 'd'), ('g', 'd').
# 3) The set() function is called again on the result of zip(s,t) to get the set of unique character pairs.
# This set represents the set of distinct character mappings between s and t.
# 4) The three set lengths are compared using the == operator to check if all the sets have the same length.
# If they do, it means that s and t are isomorphic
# because there is a one-to-one mapping between the characters in s and the characters in t.
class Solution:
    def isIsomorphic(s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))


# v1
class Solution:
    @staticmethod
    def isIsomorphic(string1: str, string2: str) -> bool:
        if string1 == string2:
            return True

        if len(string1) != len(string2):
            return False

        map1 = {}
        iso1 = ""
        for s in string1:
            if s not in map1:
                map1[s] = f"{len(map1)} "
            iso1 += map1[s]

        map2 = {}
        iso2 = ""
        for s in string2:
            if s not in map2:
                map2[s] = f"{len(map2)} "
            iso2 += map2[s]

        return iso1 == iso2


# v2 - slightly oprimized
class Solution:
    @staticmethod
    def isIsomorphic(string1: str, string2: str) -> bool:
        if string1 == string2:
            return True

        if len(string1) != len(string2):
            return False

        map1 = {}
        map2 = {}
        iso1 = ""
        iso2 = ""
        for s1, s2 in zip(string1, string2):
            if s1 not in map1:
                map1[s1] = f"{len(map1)} "
            iso1 += map1[s1]

            if s2 not in map2:
                map2[s2] = f"{len(map2)} "
            iso2 += map2[s2]

            if iso1 != iso2:
                return False

        return True


# v3: map + set
class Solution:
    @staticmethod
    def isIsomorphic(string1: str, string2: str) -> bool:
        if string1 == string2:
            return True

        if len(string1) != len(string2):
            return False

        char_map = {}
        char_set = set()
        for s1, s2 in zip(string1, string2):
            if s1 not in char_map:
                # Add a new pair of characters
                char_map[s1] = s2
                if s2 in char_set:
                    # No two characters may map to the same character!
                    return False
                # Add new unique character from string2
                char_set.add(s2)
            elif char_map[s1] != s2:
                return False

        return True


test_cases = (
    ("badc", "baba", False),
    ("egg", "add", True),
    ("foo", "bar", False),
    ("paper", "title", True),
    ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", True),
    ("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck", False),
)
for x, y, answer in test_cases:
    result = Solution.isIsomorphic(x, y)
    print(result)
    assert result == answer
