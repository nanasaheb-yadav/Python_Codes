def case1():
    print("case 1", case1.__str__())

def switch(choice):

    switcher={
        'Ram': case1(),
        'Shiv':'Tuesday'
    }
    print(switcher.get(choice,'Hi, user'))


switch('Shiv')