# Given a 32-bit signed integer, reverse digits of an integer.

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
        else:
            return result

        new_x = -int(str(x)[:0:-1]) if x < 0 else int(str(x)[::-1])
        if new_x < 2147483647 and new_x > -2147483647:
            return new_x
        else:
            return 0

"""
# v2:
def reverse(self, x):
    if x < 0:
        xstring = '-' + str(-x)[::-1]
    else:
        xstring = str(x)[::-1]
    if int(xstring) < -2147483648 or int(xstring) > 2147483647:
        return 0
    return(int(xstring))
"""

def main():
    a = Solution()
    print(a.reverse(123))
    print(a.reverse(-324236469))

import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')