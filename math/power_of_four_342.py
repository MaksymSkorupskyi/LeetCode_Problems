"""342. Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
"""

# recursion: Runtime 56 ms beats 95.94 % of python3 submissions.
class Solution:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in (1, 4):
            return True
        if n % 4 or n < 1:
            return False
        return self.isPowerOfFour(n // 4)


# cycle: Runtime 56 ms beats 95.94 % of python3 submissions.
class Solution:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 4 == 0:
            n = n / 4
        return n == 1


# bit manipulation: Runtime 56 ms beats 95.94 % of python3 submissions.
class Solution:
    def isPowerOfFour(self, n):
        test = 1
        while test < n:
            test = test << 2
        return test == n


def main():
    a = Solution()
    for i in range(-1, 21038):
        print(i, a.isPowerOfFour(i))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')