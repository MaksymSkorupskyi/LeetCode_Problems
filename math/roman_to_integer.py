"""13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def roman_to_int(s: str) -> int:
    """
    :type s: str
    :rtype: int

    exceptions{
        'IV' : 4,
        'IX' : 9,
        'XL' : 40,
        'XC' : 90,
        'CD' : 400,
        'CM' : 900}
    """
    result = 0

    if "IV" in s:
        result += 4
        s = s.replace("IV", "")

    if "IX" in s:
        result += 9
        s = s.replace("IX", "")

    if "XL" in s:
        result += 40
        s = s.replace("XL", "")

    if "XC" in s:
        result += 90
        s = s.replace("XC", "")

    if "CD" in s:
        result += 400
        s = s.replace("CD", "")

    if "CM" in s:
        result += 900
        s = s.replace("CM", "")

    for i in s:
        if i == "M":
            result += 1000
        elif i == "D":
            result += 500
        elif i == "C":
            result += 100
        elif i == "L":
            result += 50
        elif i == "X":
            result += 10
        elif i == "V":
            result += 5
        elif i == "I":
            result += 1
    return result


# It's one of my first solutions on Leetcode, so it has a lot of lines :)
# Runtime: 144 ms beats 74.02 % of python3 submissions.
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        exceptions{
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900}
        """
        result = 0

        if "IV" in s:
            result += 4
            s = s.replace("IV", "")

        if "IX" in s:
            result += 9
            s = s.replace("IX", "")

        if "XL" in s:
            result += 40
            s = s.replace("XL", "")

        if "XC" in s:
            result += 90
            s = s.replace("XC", "")

        if "CD" in s:
            result += 400
            s = s.replace("CD", "")

        if "CM" in s:
            result += 900
            s = s.replace("CM", "")

        for i in s:
            if i == "M":
                result += 1000
            elif i == "D":
                result += 500
            elif i == "C":
                result += 100
            elif i == "L":
                result += 50
            elif i == "X":
                result += 10
            elif i == "V":
                result += 5
            elif i == "I":
                result += 1
        return result


def main():
    a = Solution()
    print(a.romanToInt("DCXXI"))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
