"""139. Word Break
Medium

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False


def is_word_in_strings(word: str, strings: str | list[str]) -> (bool, list[str]):
    if isinstance(strings, list):
        for s in strings:
            return any(is_word_in_strings(word, s))

    if word in strings:
        return True, strings.split(word)

    return False, strings.split(word)


class Solution:
    @staticmethod
    def word_break(s: str, word_dict: List[str]) -> bool:
        """Given a string s and a dictionary of strings wordDict,
        return true if s can be segmented into a space-separated sequence
        of one or more dictionary words.
        """
        word_map = {}
        temp = s
        for word in word_dict:
            flag, remainder = is_word_in_strings(word, temp)
            word_map[word] = flag
            temp = remainder

            print(word, temp, word_map)

        return True


print(Solution.word_break(s="catsanddog", word_dict=["cats", "dog", "sand", "and", "cat"]))
print(Solution.word_break(s="applepenapple", word_dict=["apple", "pen"]))
print(Solution.word_break(s="leetcode", word_dict=["leet", "code"]))
print(Solution.word_break(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"]))

assert Solution.word_break(s="leetcode", word_dict=["leet", "code"]) is True
assert Solution.word_break(s="applepenapple", word_dict=["apple", "pen"]) is True
assert Solution.word_break(s="catsanddog", word_dict=["cats", "dog", "sand", "and", "cat"]) is True
assert Solution.word_break(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"]) is False
