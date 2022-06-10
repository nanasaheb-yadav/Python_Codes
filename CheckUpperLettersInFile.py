f= r"D:\Training\Cognizant Project Training\Conversion\18OCT\Errors.txt"
with open(f,"r") as file:
    data = file.read()
    cnt = 0
    for i in data:
        if i.isupper():
            cnt+=1
    print(cnt)


print(sum([1 for i in open(f,'r').read() if i.isupper()]))

print(len([i for i in open(f,'r').read() if i.isupper()]))

print(sum((1 for i in open(f,'r').read() if i.isupper())))

