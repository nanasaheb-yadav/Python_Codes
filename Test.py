"""
HCL INTERVIEW Questions
"""

e = []
o = []
for i in range(1, 100):
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)

print(f"{e}\n{o}")

name_str = ['nanasaheb', "satish"]

print(name_str[0][::-1])

print(name_str[::-1])

for i in range(len(name_str)):
    print(name_str[i][::-1])

import pandas as pd

df = pd.read_csv("test.txt", header='infer')
print(df['b'])
print(df['b'][1])


line = open("test.txt").read()

