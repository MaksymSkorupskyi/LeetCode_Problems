"""7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit
signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

# Runtime: 56 ms beats 97.98 % of python3 submissions.
class Solution:
    def reverse(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.
        :type x: int
        :rtype: int
        """
        if x < 0:
            result = -(int(str(-x)[::-1]))
        else:
            result = int(str(x)[::-1])
        if result < -2147483648 or result > 2147483647:
            return 0
        return result


def main():
    a = Solution()
    print(a.reverse(123))
    print(a.reverse(-324236469))

import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')