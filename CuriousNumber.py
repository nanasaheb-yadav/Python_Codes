"""
return number which matches to sum of factorial of each number.
like
num = 142
sum of fact of 1,4,2
if sum is same as number then return that number in list.
"""


def curious_number(num):
    cur_lst = []
    for i in range(1, num + 1):
        nums = list(map(int, list(str(i))))
        total = 0
        for dgt in nums:
            total += factorial(dgt)
        if total == num:
            cur_lst.append(num)
    return cur_lst


def factorial(num):
    if num < 0:
        return "Factorial of Negative number is not possible"
    elif num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


print(curious_number(10000))
