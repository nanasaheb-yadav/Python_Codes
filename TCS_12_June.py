# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import time
time.time()
print("Hello world")

str1 = "ABCdcdc"
str1 = list(str1)
print(str1[::-1])
print(set(str1))
substr = "cdc"


def time(fun):
    def wrap(*args, **kargs):
        starttime = time.now()
        result = fun(*args)
        total = time.now() - starttime
        return result

    return wrap


fun(a=1, b=34, c="g")

print(list(map(lambda x: x + x, str1)))

sublen = len(substr)
count = 0
for i, val in enumerate(str1):
    tempstr = str1[i:i + sublen]
    # print(tempstr)
    if substr == tempstr.lower():
        count += 1

print(count)
