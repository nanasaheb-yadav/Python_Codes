'''
Birlasoft - 21 Sept 2022

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

"""
2. Compare two versions and return the comparison result.
    * if v1 is newer than v2, return -1
    * if v1 is older than v2, return 1
    * if v1 is the same with v2, return 0
You can assume:
    * all digits in the versions are greater or equal to 0
    * the inputs will be valid strings
"""
def compareVersion(v1,v2):

    v1 = v1.split('.')
    v2 = v2.split('.')

    if len(v1) > len(v2):
        val = len(v1)- len(v2)
        for i in range(val):
            v2.append('0')
    else:
        val = len(v2)- len(v1)
        for i in range(val):
            v1.append('0')

    v1 = int("".join(v1))
    v2 = int("".join(v2))
    if v1> v2:
        return -1
    elif v1< v2:
        return 1
    else:
        return 0


print(compareVersion("1.0.0", "1.0.1"))       # 1
print(compareVersion("1", "1.0.0"))           # 0
print(compareVersion("2.0.1", "2.0.10"))      # 1
print(compareVersion("1.0.0", "2.0.0.13"))    # 1
print(compareVersion("18.0", "0.0.0.4"))      # -1
print(compareVersion("1.0.1.23", "1.0.11.1")) # 1
print(compareVersion("1.0.1.23", "1.0"))      # -1
print(compareVersion("1.0.0", "1.0"))         # 0
print(compareVersion("1.0.0.0", "1.0"))       # 0
print(compareVersion("1.0.0.2", "1.0"))       # -1

'''
# print("Hello world")

list1 = [1,2,3,4,5]

output = list(map(lambda x: x*x, list1))

print(output)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list[:1:-2]

input = 'bbaaaddcccc'
output = {'b': 2, 'a': 3, 'c': 4, 'd': 2}

count = {}

for i in input:
    count[i] = count.get(i,0)+1

print(count)


