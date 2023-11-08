"""326. Power of Three

Given an integer, write a function to determine if it is a power of three.
"""


# recursion: Runtime 472 ms beats 80.91 % of python3 submissions.
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in (1, 3):
            return True
        if n % 3 or n < 1:
            return False
        return self.isPowerOfThree(n // 3)


# cycle: Runtime 472 ms beats 80.91 % of python3 submissions.
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 3 == 0:
            n = n / 3
        return n == 1


# class Solution:
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n < 1:
#             return False
#         if n in [1, 3]:
#             return True
#         if n % 3:
#             return False
#         return self.isPowerOfThree(n // 3)


def main():
    a = Solution()
    for i in range(-2, 21038):
        print(i, a.isPowerOfThree(i))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
