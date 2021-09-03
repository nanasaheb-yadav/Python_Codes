list1 = [1,2,3,5,3,2,4,6,1]

count = {}

for i in list1:
    count[i] = count.get(i,0)+1

print(count)

"""dict1 = {}
while count:
    min = count
    for i in count.items():
        """

city = ['Pune', "Mumbai", "Benglore"]

char_list = [i[-1] for i in city]
print(char_list)

prime = lambda num: True if num/ num ==0 or num /1 ==0 else False

print(prime(5))

