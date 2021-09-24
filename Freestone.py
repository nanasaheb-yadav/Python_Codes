"""n = 7

print(n**2 )"""
data = "Hello"
d = {}

count = {}
for letter in data:
    if letter in data:
        pass
    else:
        print(letter)
        break
   #count[letter] = count.get(letter, 0) + 1

lst = [1,1,2,5]
print(tuple(lst))
names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-1])

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']

for letter in weekdays:
    count[letter] = count.get(letter, 0) + 1
print(count["mon"])

n=8
res = 0

# Add n to res n-1 times
for i in range(n):
    res += n
print(res)