# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# All string related operations
# OOPs concepts
# Inheritance
# Polumerphism


list1 = [1, 3, 2]
list2 = ["a", "b", "v"]
var = map(lambda x: x * 2, list2)
for i in var:
    print

print(map(list1, list2))

for i, j in enumerate(list1):
    print(i, j)

# print(list1 * 2)

l1 = [3, 2, 5, 4, 6]
# print( "".join([str(i) for i in l1]))

word = "abcdefghi"
word1 = "abcdefghi"
word1 = word1 + " "

print(id(word), id(word1))
print(word == word1)
print(word is word1)

print(word[:3] + word[3:])

l2 = [3, 2, 5, 4, 6]
print(id(l1), "\n", id(l2))

print(l1 == l2)
print(l1 is l2)


