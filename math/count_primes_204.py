"""204. Count Primes

Count the number of prime numbers less than a non-negative number, n.
"""

# Runtime: 216 ms beats 93.74 % of python3 submissions.
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        # generate array with n True elements: [True, True, True, True, ... True]
        primes = [True] * n
        # 0 and 1 are not primes: [False, False, True, True, ... True]
        primes[0] = primes[1] = False
        # we only need to consider factors up to √n because,
        # if n is divisible by some number p, then n = p × q and since p ≤ q, we could derive that p ≤ √n.
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]: # The Sieve of Eratosthenes - brilliant!
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

def main():
    a = Solution()
    print(a.countPrimes(3000000))

import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
