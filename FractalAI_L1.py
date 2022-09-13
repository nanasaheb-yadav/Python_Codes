print("Hello world")
x = [[1, 2], [3, 4], [5, 6]]
"""
[1, 3, 5]
[2, 4, 6]
list2 = []
list1 = []
for i in x:
    list1.append(i[0])
    list2.append(i[1])

l =[list1, list2]
print(l)"""
string1 = "Online Python compiler (interpreter) to run Python online."
data = string1.split()
count = {}
for i in data:
    count[i] = len(i)
output = sorted(count.items(), key=lambda x: x[1])
print(output[-1])
import requests

data = requests.get(url)
import selenium

webdriver(url)
id | Name | SAL
---------------------
1 | Ross | 37000
2 | Joey | 17000
3 | Monica | 47000
4 | Phoebe | 5000

SELECT
sal
from Employee order

by
SAL
DESC
limit
2 - 1, 1;

select
sal
from

(select sal from Employee order by SAL DESC limit 2)
order
by
sal
limit
1;





