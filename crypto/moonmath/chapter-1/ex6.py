"""
Exercise 6 (Long Division Algorithm): Using the programming language of your choice, write an algorithm that computes integer long division and handles all edge cases properly.
"""

"""
Long division is used to compute the integer division of two numbers.
Given two integers, dividend and divisor, the algorithm should return the quotient of the division.

Let a = dividend and b = divisor.

The equation is a = m * b + r.

m is the quotient and r is the remainder.
"""


def long_division(dividend, divisor):
    if divisor == 0:
        return ZeroDivisionError("Division by zero is undefined")
    elif dividend == 0:
        return 0
    elif dividend < divisor:
        return 0
    elif dividend == divisor:
        return 1
    elif dividend > divisor:
        quotient = 0
        if dividend > 0 and divisor > 0:
            while dividend >= divisor:
                dividend -= divisor
                quotient += 1
        elif dividend < 0 and divisor < 0:
            while dividend < 0:
                dividend -= divisor
                quotient -= 1
        elif dividend > 0 and divisor < 0:
            while dividend > 0:
                dividend += divisor
                quotient -= 1
        elif dividend < 0 and divisor > 0:
            while dividend < 0:
                dividend += divisor
                quotient -= 1
        return quotient


assert long_division(10, 2) == 5
assert long_division(10, -2) == -5
assert long_division(10, -3) == -4
assert long_division(27, 5) == 5
assert long_division(27, -5) == -6
try:
    long_division(127, 0)
except ZeroDivisionError:
    pass
