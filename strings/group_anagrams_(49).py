"""49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List, Dict, Tuple


# v1 - get()
# Runtime: 97 ms, faster than 97.14% of Python3 online submissions for Group Anagrams.
# Memory Usage: 18.2 MB, less than 50.33% of Python3 online submissions for Group Anagrams.
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams: Dict[Tuple, List[str]] = {}
    for string in strs:
        # sorted string would give us the same tuple for anagrams
        key = tuple(sorted(string))
        # add all anagrams to one bucket
        anagrams[key] = anagrams.get(key, []) + [string]

    # fetch values for all buckets
    return anagrams.values()


# v2 - setdefault()
# Runtime: 100 ms, faster than 95.12% of Python3 online submissions for Group Anagrams.
# Memory Usage: 18.8 MB, less than 36.38% of Python3 online submissions for Group Anagrams.
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams: Dict[Tuple, List[str]] = {}
    for string in strs:
        # sorted string would give us the same tuple for anagrams
        key = tuple(sorted(string))
        # add all anagrams to one bucket
        anagrams.setdefault(key, []).append(string)

    # fetch values for all buckets
    return anagrams.values()

    # return {tuple(s for s in sorted(string)): string for string in strs}
    # return [{tuple(s for s in sorted(string)): string} for string in strs]
    # return [tuple(s for s in sorted(string)) for string in strs]
    # return [[s for s in sorted(string)] for string in strs]


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
