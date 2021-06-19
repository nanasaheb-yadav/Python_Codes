"""
Author: Nanasaheb, Yadav
Date: 19/06/2021
Fibonacci Series using Recursion.
"""


def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


n = 9
print(fibonacci(n))
# OUTPUT: 34
