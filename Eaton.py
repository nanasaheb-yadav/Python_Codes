# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")

list1 = [1, 3, 7, 9, 2]

target = 3


def get_index(lst, total):
    indexes = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            val = lst[i] + lst[j]
            if val == total:
                indexes.append((i, j))

    return indexes


output = get_index(list1, target)
print(output)




list1 = [1,8,6,2,9,4]

#1= 1cm, 8=cm,  1, 4, vol=    (difference between two elements indexes) - min(height)

def max_volume(list1):
    indexes = []
    dict1 = {}
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            distance = j - i
            vol = distance * min([list1[i], list1[j]])
            dict1[vol] = (i, j)

    print(dict1)
    max1 = 0

    for i in dict1.keys():
        if i > max1:
            max1 = i
    return dict1.get(max1)

print(max_volume(list1))


