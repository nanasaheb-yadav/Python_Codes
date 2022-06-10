
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]

list.sort()
print(list)


# Solution 1

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)

#******************************************************************************************************
#Solution 2

l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print(l)

#******************************************************************************************************
#Solution 3

def sorting(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i] < li[j]:
                li[j],li[i] = li[i],li[j]
    return li

listToSort = [22,11,23,1,100,24,3,101,2,4]
print(sorting(listToSort))
