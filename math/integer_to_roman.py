"""12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""


# Runtime: 44 ms, faster than 99.32% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.3 MB, less than 53.30% of Python3 online submissions for Integer to Roman.
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert integer to a roman numeral.
        Input is guaranteed to be within the range from 1 to 3999.
        :type num: int
        :rtype: str
        """
        if not isinstance(num, int):
            raise TypeError(
                f"Invalid input: `{num}` must be an integer, got {type(num)} instead!"
            )

        roman_numeral_map = (
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        )
        roman = ""
        for numeral, integer in roman_numeral_map:
            while num >= integer:
                roman += numeral
                num -= integer
        return roman


# Runtime: 44 ms, faster than 99.41% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.4 MB, less than 31.67% of Python3 online submissions for Integer to Roman.
def int_to_roman(num: int) -> str:
    """
    Convert integer to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
    :type num: int
    :rtype: str
    """
    if not isinstance(num, int):
        raise TypeError(
            f"Invalid input: `{num}` must be an integer, got {type(num)} instead!"
        )

    roman_numeral_map = (
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    )
    roman = ""

    for numeral, integer in roman_numeral_map:
        roman += numeral * (num // integer)
        num = num % integer
        if num == 0:
            break
    return roman


# Runtime: 56 ms, faster than 93.51% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.1 MB, less than 80.51% of Python3 online submissions for Integer to Roman.
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman = ""

        for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            roman += roman_dict[i] * (num // i)
            num = num % i
            if num == 0:
                break
        return roman


def main():
    a = Solution()
    for i in range(1, 4000):
        print(i, a.intToRoman(i))


if __name__ == "__main__":
    import time

    timer = time.perf_counter()
    main()
    print(round((time.perf_counter() - timer) * 1000, 2), "ms")
