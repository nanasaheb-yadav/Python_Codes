data_ls = [3,1,4,2,1,5,8,5,2,77,3]
ls=[]

# using while loop
while data_ls:
    low = data_ls[0]
    for i in data_ls:
        if i > low:
            low = i
    ls.append(low)
    data_ls.remove(low)
print(ls)

# using swapping
l = ['f','g','a','d','b']
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)