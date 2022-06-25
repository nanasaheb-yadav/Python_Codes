x = (i for i in range(3))
for i in x:    print(i)
for i in x:    print(i)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

input = """# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it."""

count_dict = {}

for i in input.split(" "):
    count_dict[i] = count_dict.get(i, 0) + 1

sort_dict = {
for k, v in count_dict.items() sorted(count_dict, key = lambda x: x)}

print(count_dict)
import datetime

out = (lambda x:)(datetime.now())