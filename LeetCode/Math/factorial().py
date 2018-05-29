def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)


# one-liner
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


for i in range(11):
    print(factorial(i))
