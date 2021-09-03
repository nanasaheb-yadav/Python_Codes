list_val = ['ab', 'aa', 'ac', 'aa', 'a', 'b', 'd', 'c']

for passnum in range(len(list_val) - 1, 0, -1):
    for i in range(passnum):
        if list_val[i] > list_val[i + 1]:
            list_val[i], list_val[i + 1] = list_val[i + 1], list_val[i]

print(list_val)
