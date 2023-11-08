"""Given 2 integers x and y, check if x is an integer power of y"
(e.g. for x = 8 and y = 2 the answer is "true", and for x = 10 and y = 2 "false"

Algorithm:
Repeatedly divide y into x.
The first time you get a non-zero remainder you know x is not an integer power of y.
"""


def is_x_power_of_y(x, y):
    if n < 1:
        return False
    while x % y == 0:
        x = x / y
    return x == 1


print(is_x_power_of_y(1, 4))
print(is_x_power_of_y(4, 4))
print(is_x_power_of_y(16, 4))
print(is_x_power_of_y(1024, 4))
print(is_x_power_of_y(2048, 4))
