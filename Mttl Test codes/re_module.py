import re

mydata = " Revolution of the nations, for the nations."
pattern1 = r'n[a-z]+s'
pattern2 = r'of\s'

if re.findall(pattern1, mydata):
    mydata = re.sub(pattern1,'country',mydata)
if re.findall(pattern2, mydata):
    mydata = re.sub(pattern2,'by ',mydata)

print(mydata)

"""OUTPUT: 
Revolution by the country, for the country.
"""