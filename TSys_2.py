"""s = "mango"
ls = []
for i in s:

    if i == 'a':
        ls.append('o')
    else:
        ls.append(i)

s = ''.join(ls)
print(s)



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = sorted(lst, key=lambda element: element % 2 != 0)
print(lst)

for i, v in enumerate(lst):
    if v%2 !=0:
        lst.pop(i)
        lst.insert(-1, v)

print(lst)"""

import pandas as pd

df = pd.read_excel(r"C:\Users\nanas\OneDrive\Desktop\Book1.xlsx")

print(df)