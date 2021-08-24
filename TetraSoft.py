"""list1= [1,2,6,2,8,9,3]
sorted_ls = []

for i in range(len(list1)):
	for j in range(1,len(list1)+1):
		if list1[i]< list1[j]:
			sorted_ls.append(list1[i])
"""
list2= [1,2,3,4, 1,2,3,4, 5]
#output= [1,1] [2,2] [3,3] [4,4]

output = {}
ls = []
for i in list2:
	if i not in output.keys():
		output[i]= i
	else:
		#print(output.get(i))
		v = output.get(i)
		v = [v, i ]
		print(v)
		output[i] = v

print(output)
#output= { 1: [1,1], }
