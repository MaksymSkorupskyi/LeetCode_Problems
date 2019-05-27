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


if __name__ == '__main__':
    # for i in range(11):
    #     print(factorial(i))

    x = 1000

    timer = time.perf_counter()
    print(f'function: {factorial.__name__}(), "{factorial.__doc__}"')
    print([factorial(f) for f in range(x)])
    print(f'{(time.perf_counter() - timer) * 1000 :.2f} ms')
    print('-' * 80)
