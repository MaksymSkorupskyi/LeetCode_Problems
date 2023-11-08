from functools import lru_cache


# Runtime: 28 ms, faster than 99.23% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13 MB, less than 82.18% of Python3 online submissions for Fibonacci Number.
class Solution:
    @lru_cache(maxsize=512)
    def fib(self, N: int) -> int:
        """Fibonacci number (recursion with memoization)"""
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


# Runtime: 28 ms, faster than 99.23% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.4 MB, less than 5.34% of Python3 online submissions for Fibonacci Number.
class Solution:
    def fib(self, N: int) -> int:
        """Fibonacci number (dynamic solution)"""
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a + b
        return a
