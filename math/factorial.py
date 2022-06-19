import time
from functools import lru_cache


@lru_cache(maxsize=512)
def factorial(n):
    """Return factorial recursively"""
    if n < 2:
        return 1
    return n * factorial(n - 1)


# one-liner
@lru_cache(maxsize=512)
def factorial(n):
    """Return factorial recursively"""
    return 1 if n < 2 else n * factorial(n - 1)


# recursion with memoization
memo = {}


def factorial_recursive(n: int) -> int:
    """Return factorial recursively with memoization"""
    if n < 2:
        return 1
    if n not in memo:
        memo[n] = n * factorial(n - 1)
    return memo[n]


# iterative
def factorial_iterative(n: int) -> int:
    """Return factorial iteratively"""
    for i in range(1, n):
        n *= i
    return n


if __name__ == '__main__':

    x = 1000

    timer = time.perf_counter()
    print(f'factorial of {x}:')
    print(f'function: {factorial.__name__}(), "{factorial.__doc__}"')
    print([factorial(f) for f in range(x)][-1])
    print(f'function: {factorial_recursive.__name__}(), "{factorial_recursive.__doc__}"')
    print([factorial_recursive(f) for f in range(x)][-1])
    assert factorial(x) == factorial_recursive(x) == factorial_iterative(x)
    print(f'{(time.perf_counter() - timer) * 1000 :.2f} ms')
    print('-' * 80)
