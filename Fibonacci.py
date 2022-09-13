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
print(list(fibonacci(n)))




def fibforvalidation(num):
    fiblist = [0,1]

    for i in range(2,num + 1):
        fiblist.append(fiblist[i - 1] + fiblist[i - 2])
    print(fiblist)
    return fiblist


val =11
print(val in list(fibforvalidation(n)))
