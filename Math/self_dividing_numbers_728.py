"""
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

The boundaries of each input argument are 1 <= left <= right <= 10000."""


# 68ms Python one line solution (str) - beats 95.31 % of python3 submissions.
# https://leetcode.com/submissions/detail/143109966/
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [number for number in range(left, right+1) if '0' not in str(number) and all(number % int(char) == 0 for char in str(number))]
        # return [x for x in range(left, right + 1) if all(y and not x % y for y in map(int, str(x)))]

        # selfdivnums = []
        # for number in range(left, right + 1):
        #     if '0' not in str(number) and all((number % int(char) == 0 for char in str(number))):
        #             selfdivnums.append(number)
        # return selfdivnums


def main():
    a = Solution()
    print(a.selfDividingNumbers(1, 22))

import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')