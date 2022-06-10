class x(object):
    def m1(self):
        print("in m1 of x")


class y():
    def m1(self):
        print("in m1 of y")

    def m2(self):
        print("in m2 of y")


class z(x, y):
    # def m1(self):
    #     print("in m1 of z")
    def m3(self):
        print("in m3 of z")


# y1=y()
# y1.m1()
# y1.m2()
# a=y1.__hash__()
# print(a)
# z1=z()
# z1.m1()
# z1.m3()
# b=z1.__hash__()
# print(b)

z2 = z()
z2.m1()
