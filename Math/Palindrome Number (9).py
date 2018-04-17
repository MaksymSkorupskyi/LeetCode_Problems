"""9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


# Runtime: 272 ms beats 92.77 % of python3 submissions.
class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


# Runtime: 276 ms beats 89.85 % of python3 submissions.
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x > 2147483647:
            return False
        return str(x) == str(x)[::-1]


def main():
    a = Solution()
    print(a.isPalindrome(0))
    print(a.isPalindrome(2147483648))
    print(a.isPalindrome(121))
    print(a.isPalindrome(-121))
    print(a.isPalindrome(10))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
