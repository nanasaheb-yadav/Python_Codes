"""
Author: Nanasaheb, Yadav
Date: 19/06/2021
Fibonacci Series using Generators.
"""


def fibonacci(num):

    p, q=0, 1

    while p < num:
        yield p
        p, q = q, p+q

n = 10

for i in fibonacci(n):
    print(i)

