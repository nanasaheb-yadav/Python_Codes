ls = [5, 56, 2, 4, 8, 97, 2, 4, 34]
ls1 = []

for i in ls:
    if not i % 2 == 0:
        ls1.append(i)

print(ls1)

print([i for i in ls if not i % 2 == 0])


class Omniwyse:

    def __init__(self, roll, name, clas):
        self.roll = roll
        self.name = name
        self.clas = clas

    def details(self):
        print(f"{self.roll}: {self.name} : {self.clas}")


obj = Omniwyse(1, "Student1", "12th")
obj.details()


ls = [5,56,2,4,8,97,2,4,34]
ls1 = []

for i in ls:
    if not i %2 ==0:
        ls1.append(i)

print(ls1)

print([i for i in ls if not i%2==0])

class Omniwyse:

    def __init__(self, roll, name,clas):
        self.roll = roll
        self.name = name
        self.clas = clas

    def details(self):
        print(f"{self.roll}: {self.name} : {self.clas}")

obj = Omniwyse(1,"Student1", "12th")
obj.details()

