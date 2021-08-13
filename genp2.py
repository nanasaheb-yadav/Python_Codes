"""ls = [1,3,5,8,10]
target = 8


for i in range(len(ls)):
    if target == ls[i]:
        print(i)
"""
s = "I do not like using because because because is normally used for excuses"
input = s.lower().split(" ")

lst = sorted(input)

dct = {}
v =[]
for i in lst:
    if i[0] in dct.keys():
        val = dct.get(i[0])
        val1 = f"{val},{i}"
        dct[i[0]] = val1
    else:
        dct[i[0]]= i

dct1 = {}
for k, v in dct.items():
    v = list(dict.fromkeys(v.split(",")))
    dct1[k] =v


print(dct1)
str_dict = {i[0]:i for i in lst}
#print(str_dict)

