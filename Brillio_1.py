# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")

list1 = [2, 3, 4, 5, 6, 7, 8, 9]

l1 = [i for i in list1 if i % 2 == 0]
l2 = [i for i in list1 if i % 2 != 0]

# print(l1,l2)

s1 = 'silent'
s2 = 'listent'

d1 = {}
d2 = {}
for i in s1:
    d1[i] = d1.get(i, 0) + 1

for i in s2:
    d2[i] = d2.get(i, 0) + 1

# print(d1==d2)

# select * from table1 limit = int((select count(*) from table1)/2)

# convert string into dict

s = '{"a":1, "b":2}'

import json

print(json.loads(s))






