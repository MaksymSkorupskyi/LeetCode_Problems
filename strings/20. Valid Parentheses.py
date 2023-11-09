"""20. Valid Parentheses
Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    @staticmethod
    def isValid(string: str) -> bool:
        stack = []
        brackets_map = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        for s in string:
            if s in brackets_map.values():
                stack.append(s)
            elif s in brackets_map.keys():
                if not stack:
                    return False

                if stack[-1] == brackets_map[s]:
                    stack.pop(-1)
                else:
                    stack.append(s)

        return not stack


test_cases = (
    ("()", True),
    ("( )", True),
    ("()[]{}", True),
    ("(1)x[]y{ }", True),
    ("(]", False),
    ("[][]", True),
    ("[[]", False),
    ("[]][]", False),
    ("]", False),
    ("[", False),
    ("[", False),
    ("[[[]]]", True),
    ("]]][[[", False),
    ("[[[]][", False),
    ("]][[", False),
)
for brackets, answer in test_cases:
    result = Solution.isValid(brackets)
    print(result)
    assert result == answer
