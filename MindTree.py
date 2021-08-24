"""def caps(greeting):
    def greet(greeting):
        val= greeting.upper()
        return val
@caps
def greeting():
    return "good afternoon"

output = greeting()
print(output)

"""

MyList = ["b", "a", "a", "c", "b", "a", "c", 'a']

counter = {}

"""for i in MyList:
    #print(counter.get(i))
    if i in counter.keys():
        counter[i] = counter.get(i)+1
    else:
        counter[i] = 1
print(counter)"""

"""s = "How many many chocos do you have chocos ?"

s = s.split(" ")

output = list(dict.fromkeys(s))
print(" ".join(output))"""

data = {
    'success': 1,
    'page': 1,
    'result': [
        {
            'id': 1,
            'city': 'bangalore',
            'location': {
                'latitude': 12.12,
                'longitude': 13.12,
            }
        },
        {
            'id': 1,
            'city': 'mumbai',
            'location': {
                'latitude': 14.12,
                'longitude': 15.12,
            }
        },

    ],
}
'''#output-
# bangalore location is: 12.12, 13.12
# mumbai location is: 14.12, 15.12'''
"""
result = data['result']
#print(result)

for item in result:
    #print(item)
    city = item['city']
    location = item['location']
    print(f"{city} location is: {location['latitude']}, {location['latitude']}")
"""

"""import re

email = ['anusha@mindtree.com', 'pavan.99@gmail.com', 'anusha@okhdfc.co.in', 'yadav@com', 'yadav@hi.cam']
exp = "0-9a-zA-Z@a-zA-Z.com"
for mail in email:
    print(re.match(exp, mail))
"""
import requests

data = requests.get