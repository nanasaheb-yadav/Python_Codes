# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

"""
[15:08] C, VARISHTADAS
    "abc12kdf100"
​[15:08] C, VARISHTADAS
    12+100 => 112
ashdgkajhsdk12lkajskjd100
"""


class Parent():
    def parent_method(self):
        print("Parent Class")


class Child(Parent):

    def parent_method(self, param=1):
        print("Child")


str1 = "abc12kdf100"
str1 = list(str1)
numlist = []
temp = []
for i in str1:
    if not i.isnumeric():
        str1.insert(i, '_')
    else:
        pass
        # str1.remove(i)
numlist.append(temp)

"""for _ in str1:


    for i in str1:
        if i.isnumeric():
            temp.append(i)
        else:
            str1.remove(i)       
    numlist.append(temp)"""

print(numlist)
