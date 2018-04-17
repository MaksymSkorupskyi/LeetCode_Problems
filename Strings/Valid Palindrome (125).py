"""125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
"""

# Runtime: 56 ms beats 99.47 % of python3 submissions.
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        return s == s[::-1]


# The same, more explained:
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        stack = []
        for i in s:
            if i.isalnum():
                stack.append(i)
        return stack == stack[::-1]


def main():
    a = Solution()
    print(a.isPalindrome(''))
    print(a.isPalindrome("A man, a plan, a canal: Panama"))
    print(a.isPalindrome("race a car"))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')