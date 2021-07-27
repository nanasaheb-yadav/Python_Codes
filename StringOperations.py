"""
Question:
Input a string of ‘n’ characters
If the length of string is even, then create a list with split two characters as elements of list
If the length is odd, then the last split of 1 character should be appended with an underscore
For e.g.
Say input is "abcde" ( which has got odd number of characters )
Output should be: ["ab","cd","e_"]
Say input is "abcd"
Output should be: ["ab","cd"]
"""
s = "abcdehj"

s_lst = list(s)
t = []
for i in range(0, len(s_lst), 2):
    t.append(s_lst[i:i + 2])
f = []
for i in t:
    if len(i) == 1:
        i.append('_')
    r = "".join(i)
    f.append(r)
print(f)
