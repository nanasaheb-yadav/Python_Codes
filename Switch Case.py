def case1():
    print("case 1", case1.__str__())

def switch(choice):

    switcher={
        'A': case1(),
        'B':'Tuesday'
    }
    print(switcher.get(choice,'Hi, user'))


switch('A')