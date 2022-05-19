
l = list(range(100))

op = l[::3]
print(op)

[print(x) for x in l if l.index(x)%3 ==0]

for i, val in enumerate(l):
    if i%3==0:
        print(val)