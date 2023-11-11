"""383. Ransom Note
Easy
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    @staticmethod
    def canConstruct(ransom_note: str, magazine: str) -> bool:
        ransom_counter = {}
        for s in ransom_note:
            ransom_counter[s] = ransom_counter.get(s, 0) + 1

        magazine_counter = {}
        for s in magazine:
            magazine_counter[s] = magazine_counter.get(s, 0) + 1

        for k, v in ransom_counter.items():
            if k not in magazine_counter or magazine_counter[k] < v:
                return False

        return True


test_cases = (
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj", True),
)
for x, y, answer in test_cases:
    result = Solution.canConstruct(x, y)
    print(result)
    assert result == answer
