# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")
"""str1 = "POP"

#print(str1 == str1[::-1])

list1 = ["abc.py", 'def.c', 'ef.txt', 'df.cpp']

#out = {key: val for i in list1}
out = {}

for i in list1:
    #key= i.split(".")[0]
    val = i.split(".")[1]
    out[i]= val
#print(out)
out= sorted(out, key= lambda items: items[1])
#print(out)





memo = {}
for i in list2[::-1]:
    for j in list2[::-1]:
        sum = i+j
        memo[sum]= (i,j)
        if sum == target:
            #print(i,j)
        elif sum <target:
            break
"""
# print(memo)
list2 = [4, 5, 7, 8, 9, 10, 13]
target = 17
left = 0
right = len(list2) - 1

for i in range(len(list2)):
    print(i)
    total = list2[left] + list2[right] + list2[left + 1]
    if total == target:
        print(list2[left], list2[right])
        left += 1
    elif total < target:
        left += 1
    elif total > target:
        right -= 1





