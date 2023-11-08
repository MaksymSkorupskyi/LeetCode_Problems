"""231. Power of Two

Given an integer, write a function to determine if it is a power of two.
"""


# recursion: Runtime 56ms beats 97.17% of python3 submissions.
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in (1, 2):
            return True
        if n % 2 or n < 1:
            return False
        return self.isPowerOfTwo(n // 2)


# cycle: Runtime 56ms beats 97.17% of python3 submissions.
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 2 == 0:
            n = n / 2
        return n == 1


# Pyton "Lookup in Set" solution
# Runtime: 33 ms, faster than 93.38% of Python3 online submissions for Power of Two.
# Memory Usage: 13.8 MB, less than 52.94% of Python3 online submissions for Power of Two.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in {2**i for i in range(31)}


def main():
    a = Solution()
    for i in range(-1, 21038):
        print(i, a.isPowerOfTwo(i))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
