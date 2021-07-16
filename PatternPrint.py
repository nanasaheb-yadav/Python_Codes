"""
print pattern

*
**
***
****
*****
****
***
**
*

"""

a = 0
bool = True
while (a <= 5):
    if (a < 0):
        break;
    if (a == 5):
        bool = False
    if (bool):
        a = a + 1
    else:
        a = a - 1
    print("*"* a)
