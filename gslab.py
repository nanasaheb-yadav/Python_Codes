# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
"""print("Hello world")

list1 = [4,3,7,8,3,2,9]

length = len(list1)
min = list1[0]
for i in range(length-1):
    #print(min)

    if min > list1[i+1]:
        min = list1[i+1]

#print(min)

str1 = "Appli"
str2 = "Application"
str3 = "AB"
str4 = "Ap"

def matchPrefix(s1) :
    out = ''

    s1= sorted(s1, key= lambda x: len(x))
    for i in s1:
        length = len(s1[0])

        val = [i[:length] for i in s1 ]
        #print(val)
        prefix1 = val[0]
        for k in val:
            for n in range(len(k)):
                if k


    for i in s1:
        length = len(s1)



        """
for ch in range(length):
    if i[0][ch] == i[1][ch] & i[1][ch] == i[2][ch] & i[2][ch] == i[3][ch]:
        out.append(s1[i])
    elif i[0][ch] != i[1][ch] | i[1][ch] != i[2][ch] | i[2][ch] != i[3][ch]:
        break
        """


    """
        for i in range(len(str1)):
if s1[i] == s2[i]:
    out.append(s1[i])
elif s1[i] != s2[i]:
    break

return out

strlist = [str1, str2, str3, str4]
print(matchPrefix(strlist))
"""


Table 1
empname, id, sal, deptid

Table 2
deptid, deptname, deptheadid


SELECT empname FROM table1 ORDER BY sal DESC limit 1;

SELECT empname FROM table1 WHERE sal = MAX(sal);

SELECT deptname, max(sal) 
FROM table1 
INNER JOIN table2 ON 
table1.deptid = table2.deptid
Group BY table2.deptname 
ORDER BY table1.sal DESC 
LIMIT 1;











