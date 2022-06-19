"""242. Valid Anagram

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

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_memo = {}
        t_memo = {}
        for i, _ in enumerate(s):
            if s[i] not in s_memo:
                s_memo[s[i]] = 1
            else:
                s_memo[s[i]] += 1
            if t[i] not in t_memo:
                t_memo[t[i]] = 1
            else:
                t_memo[t[i]] += 1
        return s_memo == t_memo


# setdefault
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_memo = {}
        t_memo = {}
        for i, _ in enumerate(s):
            s_memo[s[i]] = s_memo.setdefault(s[i], 1) + 1
            t_memo[t[i]] = t_memo.setdefault(t[i], 1) + 1
        return s_memo == t_memo


# get
# Runtime: 57 ms, faster than 78.48% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 96.95% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_memo = {}
        t_memo = {}
        for i, _ in enumerate(s):
            s_memo[s[i]] = s_memo.get(s[i], 0) + 1
            t_memo[t[i]] = t_memo.get(t[i], 0) + 1
        return s_memo == t_memo


# Runtime: 57 ms, faster than 78.59% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.2 MB, less than 11.52% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
