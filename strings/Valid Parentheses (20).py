"""20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Empty string is also considered valid."""


# Runtime: 36 ms beats 99.85 % of python3 submissions
class Solution:
    def isValid(self, expression):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'{': 1, '}': -1,
                    '[': 2, ']': -2,
                    '(': 4, ')': -4}
        stack = []
        for i in expression:
            if stack and stack[-1] + brackets[i] == 0:
                stack.pop()
            elif brackets[i] > 0:
                stack.append(brackets[i])
            else:
                return False
        return not stack

"""
# One of my first solutions - Time Limit Exceeded :)))
def isValid(s): 
    if s == '' or len(s) % 2 != 0:
        return False
    open_brackets = ('(', '[', '{')
    close_brackets = (')', ']', '}')
    brackets_pairs = ('()', '[]', '{}')
    brackets = ('(', '[', '{', '}', ']', ')')
    brackets_errors = ('(]', '(}', '[)', '[}', '{)', '{]')
    stack = list(s)
    while len(stack) > 2:
        if stack[0] not in open_brackets or stack[len(stack)-1] not in close_brackets:
            return False
        for i in reversed(range(len(stack))):
            if len(stack) % 2 != 0:
                stack.pop(i)
            else:
                if stack[i] not in brackets:        # if len(stack) > 2 and stack[i] not in brackets:
                    return False
                elif stack[i-1] + stack[i] in brackets_errors:
                    return False
                elif stack[i-1] + stack[i] in brackets_pairs:
                    stack.pop(i)
    if not stack:
        return True
    elif stack[0] + stack[1] in brackets_pairs:
        return True
    else:
        return False
"""

def main():
    a = Solution()
    print(a.isValid(''))
    print(a.isValid('[]'))
    print(a.isValid('([])'))
    print(a.isValid('['))
    print(a.isValid(']'))
    print(a.isValid('([)]'))

import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')