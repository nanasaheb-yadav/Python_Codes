# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

n = 12345
l1 = [1, 2, 3, 4]
l2 = [2, 4, 7, 8]
tuple1 = (2, 4, 31, 5, 6, 3, 9)


dict1 = {}

for i in tuple1:
    dict1[i] = i ** 2
print(dict1)

list1 = [i for i in l1 if i in l2]
print(list1)

# print(str(n)[::-1])

d1 = {'a': 15, 'b': 12}
d2 = {'b': 5, 'c': 3, 'd': 15}

for i in d1.keys():
    if i in d2.keys():
        d2[i] = d2.get(i) + d1.get(i)
    else:
        d2[i] = d1.get(i)

print(d2)

# output
# d = {'a':15,'b':17,'c':3,'d':15}

# class Maths:

# def sqrt(self, number):

#   result = number