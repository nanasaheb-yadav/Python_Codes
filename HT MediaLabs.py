# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

"""Input
file.csv
400102,b-1,india
400102,b-2,india
400102,b-2,india
400103,b-1,india

O/P
in 400102 total uni number of building are 2
in 400103 total uni number of building are 1"""

data = open("file1.csv", 'r').read()
list1 = []
count = {}
for line in data:
    ls1 = line.split(',')
    #list1.append(ls1)
    count[ls1[0]]= count.get(ls1[0],0)+1




