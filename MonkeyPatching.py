class A:
    def func(self):
        print("Hi")
    def monkey(self):
        print("Hi, monkey")


m = A()

m.func = m.monkey

m.func()