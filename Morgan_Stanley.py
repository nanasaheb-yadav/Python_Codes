
import pandas as pd

data1 = {"a":[1,2,3],"b":['a','r',None], "date": ["20-02-2021", "22-02-2021","12-03-2021"]}

data2 = {"c":[4,7,8], "d":['q','y','r']}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
"""df = df1.join(df2)
#print(df)
d = df[df['b'].notnull()]
print(d)"""
# df = df1.grouper(key= 'date',freq='M')
# print(df)

df1['d'] = df1['a'].apply(lambda x: x+1 if x%2==0 else x-1)
#print(df1)

tuple1 = (1,4,6,2)
tuple2 = (5,4,3,2)

lst = list(zip(tuple1,tuple2))
#print(lst)
s = 'ababaacklcmnn'
d ={}

for i in s:
    val = s.count(i)
    if val == 1:
        #print(i)
        break

list1 = [233,26,7,74,9,536,11]
#list1= [233,26,11]
sum = []
for i in range(len(list1)):
    for j in range(len(list1)):
        list1[i], list1[j] =list1[j], list1[i]

        val = ''.join(map(str,list1))
        #print(val)
        sum.append(int(val))

ls= sorted(sum)
print(ls)
print(ls[-1])

