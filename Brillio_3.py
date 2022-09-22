"""
EClerx 1st interview - 21 Sept 2022


"""
s= "Pune, Mumbai, Benglore, Chennai"
print(", ".join(s.split(',')[::-1]))

def f1():
    print("hello")

def f2(a,b):
    print(a)
    print(b)

f2(f1,10)  #output: 10
f2(f1(),10)
