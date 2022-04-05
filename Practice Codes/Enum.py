"""a= 2
b = 5

Input='Tata Technologies Limited'
# Output='ataT seigolonhceT detimiL'
Input = Input.upper()
Input = Input.replace(' ','')
ip = Input.split(' ')


count={}

for i in Input:

    count[i] = count.get(i, 0)+1

print(count )"""

a=1
b=1
list1=[1,2,3]
list2=[1,2,3]
print(list1 is list2)
print(list1==list2)
print(a is b)
print(a==b)
list1=[1,2,3]
list2=[1,2,3]
#list1.append(list2)
list1.extend(list2)
print(list1)

max = lambda a,b : a if a>b else b
max(1,2)