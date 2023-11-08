"""125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
"""


# Runtime: 44 ms, faster than 98.26% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.4 MB, less than 32.46% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        return s == s[::-1]


# Runtime: 48 ms, faster than 94.41% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14 MB, less than 41.85% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        return not any(x != y for x, y in zip(s, reversed(s)))


# Runtime: 48 ms, faster than 94.41% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14 MB, less than 40.27% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        return all(x == y for x, y in zip(s, reversed(s)))


def main():
    a = Solution()
    print(a.isPalindrome(""))
    print(a.isPalindrome("A man, a plan, a canal: Panama"))
    print(a.isPalindrome("race a car"))


if __name__ == "__main__":
    import time

    timer = time.perf_counter()
    main()
    print(round((time.perf_counter() - timer) * 1000, 2), "ms")
