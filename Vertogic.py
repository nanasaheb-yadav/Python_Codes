"""Vertogic interview questions 27/July/2021"""

class Vertogic():

    def __init__(self):
        self.str = "Welcome to Python Developer Interview"

    var = ''

    def split_join(self, ip_str=''):
        global var
        # str1 = ip_str.split(' ')
        var = "Hello"
        return ','.join(ip_str.split(' '))


obj = Vertogic()
ip = input("Enter String: \n")
output = obj.split_join(ip)
print(output)
