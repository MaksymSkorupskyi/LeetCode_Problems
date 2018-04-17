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


def main():
    a = Solution()
    for i in range(-1, 21038):
        print(i, a.isPowerOfTwo(i))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')