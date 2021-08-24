"""
Factorial of number using recursion
"""


def factorial(num):
    if num < 0:
        return "Factorial of Negative number is not possible"
    elif num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))


fact = lambda n:1 if n==0 else n*fact(n-1)

print(fact(5))